# -*- coding: utf-8 -*-

import scipy.io.wavfile as wavfile
import librosa

TMP_IN="/tmp/in.wav"
TMP_OUT="/tmp/out.wav"


def getWavSignal(fs,signal):
    wavfile.write(TMP_IN, fs, signal)
    new_signal,sr = librosa.load(TMP_IN,sr=fs)
    assert (signal.shape==new_signal.shape)
    return new_signal
    