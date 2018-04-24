from scipy.io import wavfile
from scipy import signal
#import matplotlib.pyplot as plt
import librosa

def read_wav(fname):
    fs, signal = wavfile.read(fname)
    if (signal.shape!=1): signal=convert_audio_to_mono(signal)
    assert len(signal.shape) == 1, "Supports only mono wav file"
    return fs, signal

def convert_audio_to_mono(signal):
    return librosa.to_mono(signal)

def get_spectrogram(sample_rate, samples):
    frequencies, times, spect = signal.spectrogram(samples, sample_rate)
    return frequencies, times, spect


# def show_spectrogram(frequencies, times, spect):
#     plt.pcolormesh(times, frequencies, np.log10(spect+1), cmap='inferno')
#     # plt.imshow(spect)
#     plt.ylabel('Frequency [Hz]')
#     plt.xlabel('Time [sec]')
#     plt.show()
    
