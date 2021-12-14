from numpy.fft import fft
from scipy import signal
from scipy.fft import fftshift
import matplotlib.pyplot as plt
import numpy as np
import json
from scipy.io import wavfile
from os import path
from pydub import AudioSegment
from matplotlib.colors import Normalize 
# import seaborn as sns

# import files
piano_3 = "assets/piano3.wav"
audio_tone = "assets/100hz.wav"
bread = "assets/bread.mp3"
shepard = "assets/Shepard Tone.wav"
wine = "assets/Hozier - Cherry Wine - Cover (Fingerstyle Guitar).wav"


# Code for converting Mp3 to Wav file. Need to add other conversions and type checking in the future.
# sound = AudioSegment.from_mp3(shepard)
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
sample_rate, samples = wavfile.read(wine)
print("sample_rate:", sample_rate)

if len(samples[0]) == 2:
	print("moving from duo to mono...")
	samples = np.asarray(samples)
	samples = samples[:,0]
	print(samples)

Pxx, freqs, bins, im = plt.specgram(samples, NFFT=1024, Fs=sample_rate, noverlap=128, scale="dB")
# plt.ylim((0, 20000))
# plt.yscale('symlog')
# plt.xscale('log')
# plt.show()

print(np.shape(Pxx))
print(np.shape(freqs))
print(np.shape(bins))

Pxx_dB = 10*np.log(Pxx) # Convert to dB scale
plt.imshow(Pxx_dB, aspect='auto', origin='lower')
plt.show()
# print("exporing data...")

data = {}
data['Pxx'] = Pxx.tolist()
data['dB'] = Pxx_dB.tolist()
data['freqs'] = freqs.tolist()
data['bins'] = bins.tolist()

with open('ch_wine.txt', 'w') as outfile:
    json.dump(data, outfile)







print("closing program...")














