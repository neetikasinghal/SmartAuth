# -*- coding: utf-8 -*-

from sys import byteorder
from array import array
from struct import pack


import pyaudio
import wave
import time

THRESHOLD = 100
CHUNK_SIZE = 2048
FORMAT = pyaudio.paInt16
RATE = 44100

    
def check_if_silent(snd_data):
    "Checks if it is below the threshold"
    return max(snd_data) < THRESHOLD

def normalize(snd_data):
    "Make the volume to average"
    MAXIMUM = 16384
    times = float(MAXIMUM)/max(abs(i) for i in snd_data)
    r = array('h')
    for i in snd_data:
        r.append(int(i*times))
    return r

def trim(snd_data):
    "Trim the blank spots at the start and end"
    def _trim(snd_data):
        snd_started = False
        r = array('h')

        for i in snd_data:
            if not snd_started and abs(i)>THRESHOLD:
                snd_started = True
                r.append(i)

            elif snd_started:
                r.append(i)
        return r

    # Trim to the left
    snd_data = _trim(snd_data)

    # Trim to the right
    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data

def record():
    """
    Record a word or words from the microphone and 
    return the data as an array of signed shorts.

    Normalizes the audio, trims silence from the 
    start and end, and pads with 0.5 seconds of 
    blank sound to make sure VLC et al can play 
    it without getting chopped off.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True,
        frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    snd_started = False

    r = array('h')

    now = time.time()
    future = now + 20
    while time.time() < future:
        # little endian, signed short
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)

        silent = check_if_silent(snd_data)

#        print("isSilent? ",silent," and started? ",snd_started)
        if silent and snd_started:
            num_silent += 1
        elif not silent and not snd_started:
            snd_started = True

        if snd_started and num_silent > 10:
            break
        
        pass

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    r = normalize(r)
    r = trim(r)
    return sample_width, r

def record_to_file(path):
    "Records and outputs the resulting data to 'path'"
    sample_width, data = record()
    data = pack('<' + ('h'*len(data)), *data)

    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()

# Print  progress
def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Prints a progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()
         
def getsentence(n):
    if (n<=2):
        print ("")
        print ("")
        print (" The hungry purple dinosaur ate the kind, zingy fox,")
        print ("    the jabbering crab, and the mad whale ")
        print ("    and started vending and quacking.")
        print ("")
        print ("")
    else:
        print ("")
        print ("")
        print (" That quick beige fox jumped in the air over each thin dog. ")
        print ("    Look out, I shout, for he's foiled you again, creating chaos.")
        print ("")
        print ("")

def record_multiple_times(n):
    items = list(range(0, 57))
    l = len(items)
    getsentence(n)
    printProgress(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    record_to_file('recording'+str(n)+'.wav')
    for i, item in enumerate(items):
        time.sleep(0.1)
        printProgress(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    
    
