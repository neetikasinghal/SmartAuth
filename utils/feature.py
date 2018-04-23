# -*- coding: utf-8 -*-
import os
import glob
import sys
import librosa
import numpy as np
import scipy.io.wavfile as wavfile

from utils import filter
from utils import writetmp

SAMPLING_RATE = 44100
def process_signal(path_to_signal):
    # read all the signals from the path given
    # for each 
    #   1. remove Silence
    #   2. Reduce Noise
    #   3. extract features
    print(os.path.abspath(os.curdir))
    os.chmod(os.curdir,mode=0o777)
    if (os.path.abspath(os.curdir).endswith(path_to_signal)):
        os.chdir("../")
    abspath=os.path.abspath(path_to_signal)
    if (not os.path.isdir(abspath)):
        print("No enrolled user found!")
        sys.exit(1)
    label = os.path.basename(abspath.rstrip('/'))
    wavs = glob.glob(abspath + '/*.wav')
    if len(wavs) == 0:
        print("No wav file found in {0}".format(abspath))
    print("Enrolled User {0} has files {1}".format(label, ','.join(wavs)))
    for wav in wavs:
        fs,signal = wavfile.read(wav)
        assert len(signal.shape) == 1, "Only Support Mono Wav File!"
        signal=filter.remove_silence(fs,signal) #1 Remove Silence
        signal=filter.reduce_noise(fs,signal) #2 Reduce Noise
        features = get_spectral_features(fs,signal) #3 Extract features
    return path_to_signal, features

def get_signal(user,dir):
    wav="{0}/{1}/{2}/recording2.wav".format(os.path.abspath(os.curdir),user,dir)
    fs, signal = wavfile.read(wav)
    assert len(signal.shape) == 1, "Only Support Mono Wav File!"
    signal = filter.remove_silence(fs, signal)  # 1 Remove Silence
    signal = filter.reduce_noise(fs, signal)  # 2 Reduce Noise
    features = get_spectral_features(fs, signal)  # 3 Extract features
    return (user,features)
        
def convert_audio_to_mono(signal):
    return librosa.to_mono(signal)

def monoform(signal):
    if signal.ndim > 1:
        print("INFO: Input signal has more than 1 channel; the channels will be averaged.")
        signal = np.mean(signal, axis=1)
    return signal
    
def get_spectral_features(fs,signal):
    signal=writetmp.getWavSignal(fs,signal)
    mfcc = get_mfcc(signal)
    spectral_centroid = get_spectral_centroid(signal)
    chroma_stft = get_chroma(signal)
    #print("MFCC Shape: {0}".format(mfcc.shape))
    #print("Spectral centroid Shape: {0}".format(spectral_centroid.shape))
    #print("Chroma stft Shape: {0}".format(chroma_stft.shape))
#    return np.concatenate((mfcc),axis=1)
    mel = get_mel_spectrogram(signal)
    return np.concatenate((mfcc, mel), axis=0)

def get_mfcc(signal):
    signal=monoform(signal)
    mfcc = np.mean(librosa.feature.mfcc(signal,sr=SAMPLING_RATE,n_mels=128,fmax=8000,n_mfcc=40).T,axis=0,keepdims=True)
    # print ("MFCC shape:{}".format(mfcc.shape))
    return mfcc.T

def get_spectral_centroid(signal):
    signal=monoform(signal)
    S, phase = librosa.magphase(librosa.stft(y=signal))
    return librosa.feature.spectral_centroid(S=S)

def get_chroma(signal):
    signal=monoform(signal)
    return librosa.feature.chroma_stft(y=signal, sr=SAMPLING_RATE)

def get_mel_spectrogram(signal):
    signal = monoform(signal)
    D = np.abs(librosa.stft(signal))**2
    orig_mel=librosa.feature.melspectrogram(S=D)
    mel = np.mean(orig_mel.T,axis=0,keepdims=True)
    # print ("Mel Spectrogram orig shape:{}".format(orig_mel.shape))
    # print ("Mel Spectrogram shape:{}".format(mel.shape))
    # print ("Mel Spectrogram T shape:{}".format(mel.T.shape))
    return mel.T