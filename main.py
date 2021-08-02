from numpy.fft import fft
from scipy import signal
from scipy.fft import fftshift
import matplotlib.pyplot as plt
import numpy as np
import json
from scipy.io import wavfile
from os import path
from pydub import AudioSegment

# import files
piano_3 = "assets/piano3.wav"
audio_tone = "assets/100hz.wav"
bread = "assets/bread.mp3"


# Code for converting Mp3 to Wav file. Need to add other conversions and type checking in the future.
# sound = AudioSegment.from_mp3(src)
# sound = sound.set_channels(1)
# sound = sound.set_frame_rate(5000) # sample rate in kHz, higher sample rate, longer spectrogram computation takes
# sound.export(dst, format="wav")
# AudioSegment.frame_rate

# sound = AudioSegment.from_mp3(bread)
# sound = sound.set_channels(1)
# sound = sound.set_frame_rate(5000)
# sample_rate = AudioSegment.frame_rate
# samples = sound.raw_data

# Reading Wav file. Must be Mono (single channel)
sample_rate, samples = wavfile.read(piano_3)
print("sample_rate:", sample_rate)

# print(f"samples:\n{samples}")
# print(len(samples))
# sample_rate = len(samples)
# print(samples.tolist())

Pxx, freqs, bins, im = plt.specgram(samples, NFFT=1024, Fs=sample_rate, noverlap=900)
# plt.ylim((0, 20000))
# plt.yscale('symlog')
# plt.xscale('log')
plt.show()

# print("exporing data...")

# data = {}
# data['f'] = f.tolist()
# data['t'] = t.tolist()
# data['Sxx'] = Sxx.tolist()

# with open('data.txt', 'w') as outfile:
#     json.dump(data, outfile)

print("closing program...")