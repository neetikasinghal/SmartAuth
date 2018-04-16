from utils import recordaudio
from utils import fileread
from utils import feature
import os
from time import sleep

class SmartAuthInterface(object):
    
    def enrollinterface(self,dir):
        self.readRecording(dir)
        self.enrollModelling(dir)
    
    def authenticateinterface(self,dir):
        print("need more coding")
        
    def enrollModelling(self,dir):
        user_features=feature.process_signal(dir)
        #print (user_features)
    
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
        
        
        
    def convert_audio(self,path_to_file):
        sample_rate, samples = fileread.read_wav(path_to_file)
        freq,time,spect = fileread.get_spectrogram(sample_rate,samples)
        fileread.show_spectrogram(freq,time,spect)