# from numpy.fft import fft
# from scipy import signal
# from scipy.fft import fftshift
# import matplotlib.pyplot as plt
# import numpy as np
import json
# from scipy.io import wavfile
# from os import path
# from pydub import AudioSegment
# from matplotlib.colors import Normalize 
# import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import threading
from pydub.playback import play
from pydub import AudioSegment
import time

import pandas as pd

data_path = 'ch_wine.txt'
data = {}
with open(data_path, 'r') as infile:
    data = json.load(infile)
pxx_data = data['Pxx']
db_data = data['dB']
freqs = data['freqs']

db_df = pd.DataFrame(np.asarray(pxx_data), index=freqs)
db_amp_slice = (db_df + min(db_df))[100:300].sum()#.rolling(window=1, min_periods=0).mean().fillna(0)


# plt.plot(db_amp_slice)
# plt.show()


# Plot Spec
# plt.imshow(db_df, aspect='auto', origin='lower')
# plt.show()
# exit()

# Getting a single frequency's dB data over the course of audio
desired_frequency = 1000
target_index = int((desired_frequency / max(freqs)) * len(freqs))
# print(len(db_data[target_index]))

# Animation Vars
size = 10

# Plot Stuff
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])
scat = ax.scatter([0.5], [0.5], s=[size], lw=0.5, edgecolors=(0, 0, 0, 1), facecolors='blue')#, facecolors='none')

ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])

# Music stuff
sound = AudioSegment.from_wav("assets/Hozier - Cherry Wine - Cover (Fingerstyle Guitar).wav")
music_thread = threading.Thread(target=play, args=(sound,))
song_length = sound.duration_seconds

global music_start
music_start = 0
def update(frame_number):
    global music_start

    if frame_number == 0:
        music_thread.start()
        music_start = time.perf_counter()

    print('music_start', music_start)
    i = (time.perf_counter() - music_start)/song_length
    print('i', i)
    print(len(db_amp_slice))
    i = round(i * len(db_amp_slice))
    print(frame_number, i)

    size = db_amp_slice[i]
    # size = db_data[target_index][frame_number]
    # if size > 1000:
    #     size = 1000
    # if size < 0:
    #     size = 0
    print('size', size)
    scat.set_sizes([size])

animation = FuncAnimation(fig, update, interval=5)
plt.show()


print("closing program...")














