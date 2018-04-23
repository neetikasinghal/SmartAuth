import os
from time import sleep

from utils import feature
from utils import fileread
from utils import recordaudio
from utils import model


class SmartAuthInterface(object):
    
    def enrollinterface(self,dir):
        self.readRecording(dir)
        self.enrollModelling(dir)
    
    def authenticateinterface(self,user,dir):
        self.authRecording(user,dir)
        self.authenticateModelling(user,dir)

    def authenticateModelling(self,user,dir):
        authfolder="{0}/{1}/".format(user,dir)
        # print(authfolder)
        user_features=feature.get_signal(user,dir)
        print(user_features[1].shape)
        m = model.GMMmodel()
        m.validate_model(user_features[0],user_features[1])
        # m.validate_model_all(user_features[0],user_features[1])


    def enrollModelling(self,dir):
        user_features=feature.process_signal(dir)
        m = model.GMMmodel()
        m.generate_model(user_features[0],user_features[1])
    
    def readRecording(self,dir):
        if not os.path.exists(dir):
            os.makedirs(dir)
        os.chdir(dir)
        
        sleep(1)
        print ("You are about to start enrollment.....")
        sleep(5)
        print ("Read the below text to start...")
        sleep(5)
        recordaudio.record_multiple_times(1)
        print ("We want to identify you accurately... Lets try one more time..")
        sleep(1)
        print ("Read the below text to start...")
        sleep(2)
        recordaudio.record_multiple_times(2)
        print ("Now, this is final and we are done !!")
        sleep(1)
        print ("Read the below text to start...")
        sleep(2)
        recordaudio.record_multiple_times(3)

    def authRecording(self, user,dir):
        curdir = os.path.abspath(os.curdir)
        authfolder="{0}/{1}".format(user,dir)
        if not os.path.exists(authfolder):
            os.makedirs(authfolder)
        os.chdir(authfolder)

        sleep(1)
        print ("Welcome...")
        sleep(5)
        print ("Read the below text to authenticate...")
        sleep(5)
        recordaudio.record_multiple_times(2)
        
        os.chdir(curdir)
        
    def convert_audio(self,path_to_file):
        sample_rate, samples = fileread.read_wav(path_to_file)
        freq,time,spect = fileread.get_spectrogram(sample_rate,samples)
        fileread.show_spectrogram(freq,time,spect)