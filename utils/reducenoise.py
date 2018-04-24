# -*- coding: utf-8 -*-

from random import Random
import scipy.io.wavfile as wavfile
import os

NOISE_WAV = "/tmp/noise.wav"
NOISE_MODEL = "/tmp/noise.prof"
THRES = 0.21
r = Random()
class NoiseFilter(object):

    def init_noise(self, fs, signal):
        wavfile.write(NOISE_WAV, fs, signal)
        os.system("sox {0} -n noiseprof {1}".format(NOISE_WAV, NOISE_MODEL))

    def filter(self, fs, signal):
        rand = r.randint(1, 100000)
        fname = "/tmp/tmp{0}.wav".format(rand)
        signal = self.monoform(signal)
        wavfile.write(fname, fs, signal)
        fname_clean = "/tmp/tmp{0}-clean.wav".format(rand)
        os.system("sox -v 0.99 {0} {1} noisered {2} {3}".format(fname, fname_clean,NOISE_MODEL,THRES))
        fs, signal = wavfile.read(fname_clean)
        signal = self.monoform(signal)
        os.remove(fname)
        os.remove(fname_clean)
        return signal
    
    def monoform(self,signal):
        if signal.ndim > 1:
            signal = signal[:,0]
        return signal
