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
src = "piano2.wav"
# dst = "test.wav"
dst = "piano3.wav"

print("converting to wav file...")
# sound = AudioSegment.from_mp3(src)
# sound = sound.set_channels(1)
# sound.export(dst, format="wav")

sound = AudioSegment.from_wav(src)
print(sound.duration_seconds)
sound = sound.set_channels(1)
sound = sound.set_frame_rate(5000)
sound.export(dst, format="wav")

print("importing wav file...")
sample_rate, samples = wavfile.read(dst)
print(f"sample_rate:\n{sample_rate}")
print(f"samples:\n{samples}")
print(len(samples))
# sample_rate = 1000
# print(samples.tolist())

# rng = np.random.default_rng()

# # Generate a test signal, a 2 Vrms sine wave whose frequency is slowly modulated around 3kHz, corrupted by white noise of exponentially decreasing magnitude sampled at 10 kHz.
# fs = 10e3
# N = 1e5
# amp = 2 * np.sqrt(2)
# noise_power = 0.01 * fs / 2
# time = np.arange(N) / float(fs)
# mod = 500*np.cos(2*np.pi*0.25*time)
# carrier = amp * np.sin(2*np.pi*3e3*time + mod)
# noise = rng.normal(scale=np.sqrt(noise_power), size=time.shape)
# noise *= np.exp(-time/5)
# x = carrier + noise

# # Compute and plot the spectrogram.
# f, t, Sxx = signal.spectrogram(x, fs)

print("making spectrogram...")
f, t, Sxx = signal.spectrogram(samples, sample_rate)
print(f"f:\n{f}")
print(f"t:\n{t}")
print(f"Sxx:\n{Sxx}")

print("making graph...")
# plt.pcolormesh(t, f, Sxx, shading='gouraud')
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.show()

plt.pcolormesh(t, f, Sxx, shading='gouraud')
plt.imshow(Sxx)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

print("exporing data...")

# data = {}
# data['f'] = f.tolist()
# data['t'] = t.tolist()
# data['Sxx'] = Sxx.tolist()

# with open('data.txt', 'w') as outfile:
#     json.dump(data, outfile)