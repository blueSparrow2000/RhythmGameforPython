'''
This file makes ai charts given a music!

1. Music file given to music21 module
2. Get script
3. Translate script to chart pattern

I made a code which does part 3.

import os, sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile # get the api
import plotly.graph_objects as go

import numpy as np
import tqdm

from chart_builder import *

VERBOSE = False

current_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
ai_song_name = "NyanCat (Neuro)_A"

MUSIC_FOLDER = current_dir+'/cc_musics/' #'/sound_effects/'
AUDIO_FILE = "{}.wav".format(ai_song_name)

APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0])) + '/charts/'
full_path = os.path.join(APP_FOLDER, '%s.txt' % ai_song_name)



# Configuration
FPS = 120
FFT_WINDOW_SECONDS = 0.1#0.25 # how many seconds of audio make up an FFT window

# Note range to display
FREQ_MIN = 10
FREQ_MAX = 1000

# Notes to display
TOP_NOTES = 1 # 3

# Names of the notes
NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
NOTE_DICT = {NOTE_NAMES[i]:i for i in range(len(NOTE_NAMES))}

# Output size. Generally use SCALE for higher res, unless you need a non-standard aspect ratio.
RESOLUTION = (1920, 1080)
SCALE = 2 # 0.5=QHD(960x540), 1=HD(1920x1080), 2=4K(3840x2160)

########################### Adjusting parameter
beat_window_size = 4
beat_offset = 0 #80 # ms
beatpos_final_offset = -500
###########################

# See https://newt.phys.unsw.edu.au/jw/notes.html
def freq_to_number(f): return 69 + 12 * np.log2(f / 440.0)

def number_to_freq(n): return 440 * 2.0 ** ((n - 69) / 12.0)

def note_name(n): return NOTE_NAMES[n % 12] + str(int(n / 12 - 1))


def plot_fft(p, xf, fs, notes, dimensions=(960, 540)):
    layout = go.Layout(
        title="frequency spectrum",
        autosize=False,
        width=dimensions[0],
        height=dimensions[1],
        xaxis_title="Frequency (note)",
        yaxis_title="Magnitude",
        font={'size': 24}
    )

    fig = go.Figure(layout=layout,
                    layout_xaxis_range=[FREQ_MIN, FREQ_MAX],
                    layout_yaxis_range=[0, 1]
                    )

    fig.add_trace(go.Scatter(
        x=xf,
        y=p))

    for note in notes:
        fig.add_annotation(x=note[0] + 10, y=note[2],
                           text=note[1],
                           font={'size': 48},
                           showarrow=False)
    return fig


def extract_sample(audio, frame_number):
    end = frame_number * FRAME_OFFSET
    begin = int(end - FFT_WINDOW_SIZE)

    if end == 0:
        # We have no audio yet, return all zeros (very beginning)
        return np.zeros((np.abs(begin)), dtype=float)
    elif begin < 0:
        # We have some audio, padd with zeros
        return np.concatenate([np.zeros((np.abs(begin)), dtype=float), audio[0:end]])
    else:
        # Usually this happens, return the next sample
        return audio[begin:end]


def find_top_notes(fft, num):
    if np.max(fft.real) < 0.001:
        return []

    lst = [x for x in enumerate(fft.real)]
    lst = sorted(lst, key=lambda x: x[1], reverse=True)

    idx = 0
    found = []
    found_note = set()
    while ((idx < len(lst)) and (len(found) < num)):
        f = xf[lst[idx][0]]
        y = lst[idx][1]
        n = freq_to_number(f)
        n0 = int(round(n))
        name = note_name(n0)

        if name not in found_note: # remove duplicate
            found_note.add(name)
            s = [f, note_name(n0), y]
            found.append(s)
        idx += 1

    return found



fs, data = wavfile.read(os.path.join(MUSIC_FOLDER,AUDIO_FILE)) # load the data
audio = data.T[0] # this is a two channel soundtrack, get the first track
FRAME_STEP = (fs / FPS) # audio samples per video frame
FFT_WINDOW_SIZE = int(fs * FFT_WINDOW_SECONDS)
AUDIO_LENGTH = len(audio)/fs


# Hanning window function
window = 0.5 * (1 - np.cos(np.linspace(0, 2 * np.pi, FFT_WINDOW_SIZE, False)))

xf = np.fft.rfftfreq(FFT_WINDOW_SIZE, 1 / fs) # frequency
FRAME_COUNT = int(AUDIO_LENGTH * FPS)
FRAME_OFFSET = int(len(audio) / FRAME_COUNT)
TOTAL_AUDIO_LEN = int(len(audio)*2/100)
frame_ms = round(len(audio)/FRAME_COUNT)*2/100

if VERBOSE:
    print("en(audio): ", len(audio))
    print("FFT_WINDOW_SIZE: ",FFT_WINDOW_SIZE)
    print("FRAME_COUNT: ",FRAME_COUNT)
    print("FRAME_OFFSET: ",FRAME_OFFSET)
    print("FRAME_STEP: ",FRAME_STEP)
    print("mili-sec per frame: ",frame_ms)
########################
def check_all_equal(list):
    return all(i[0] == list[0][0] for i in list)

def find_first_beatpos(list):
    bp = list[0][1]
    for i in range(len(list)):
        if list[i][1] < bp:
            bp = list[i][1]
    return bp

def initialize_beatwindow():
    return [[None,None,None] for i in range(beat_window_size)]

def find_highest_intensity_beatpos(list):
    new_list = sorted(list, key=lambda elem: elem[2]) # sort by intensity
    return new_list[-1][1]  # beatpos of the highest intensity




beat_list = []
beat_window = initialize_beatwindow()
beat_index = 0


# Pass 1, find out the maximum amplitude so we can scale.
mx = 0
for frame_number in range(FRAME_COUNT):
    sample = extract_sample(audio, frame_number)

    fft = np.fft.rfft(sample * window)
    fft = np.abs(fft).real
    mx = max(np.max(fft), mx)

print(f"Max amplitude: {mx}")



# Pass 2, produce the animation
for frame_number in tqdm.tqdm(range(FRAME_COUNT)):
    sample = extract_sample(audio, frame_number)

    fft = np.fft.rfft(sample * window)
    fft = np.abs(fft) / mx

    s = find_top_notes(fft, TOP_NOTES)
    if VERBOSE:
        print(frame_number, end=' ')
        print(s, end='')

    if s == []:
        continue

    note = s[0][1]
    intensity = s[0][2]
    beatpos = beat_offset + frame_number * frame_ms
    beat_window[frame_number%beat_window_size] = (note,beatpos,intensity)
    if VERBOSE:
        print(" Beat window: ",beat_window)

    if check_all_equal(beat_window):
        beat_list.append([note,find_first_beatpos(beat_window)])
        #beat_list.append([note, find_highest_intensity_beatpos(beat_window)])

        beat_window = initialize_beatwindow() # reset
        if VERBOSE:
            print("reset!")

    # fig = plot_fft(fft.real, xf, fs, s, RESOLUTION)
    # fig.write_image(current_dir + f"/content/frame{frame_number}.png", scale=2)

if VERBOSE:
    print("done!")
    print(beat_list)

def note_to_lane(note_str):
    octave = int(note_str[-1])
    code = note_str[0]
    if len(note_str)==3:
        code = note_str[0:2]

    code_value = NOTE_DICT[code] # 0 to 11
    # octave = 12? will be better?
    # lane = 4
    return (octave*8 + code_value)%4 + 1

def to_pattern(lane,beatpos):
    return basic_strike(round(beatpos)+beatpos_final_offset,lane,1,special = '')



beat_list_lane = [(note_to_lane(beat[0]),beat[1]) for beat in beat_list]

beat_precision = 300 # 100 ms
precision_window_size = 2
def init_precision_window():
    return [[None, None] for i in range(precision_window_size)]

for k in range(10):
    rmv_cnt = 0
    ########################### one pass
    precision_window = init_precision_window()
    precision_cnt = 0
    for beat_elem in beat_list_lane:
        precision_window[precision_cnt%precision_window_size] = beat_elem

        if check_all_equal(precision_window):
            beat_prior = precision_window[(precision_cnt - 1) % precision_window_size]
            if abs( beat_prior[1] - beat_elem[1]) < beat_precision:
                #print(precision_window)
                # change the beat list!

                #beat_list_lane.remove(beat_prior)
                beat_list_lane.remove(beat_elem)
                rmv_cnt +=1

            precision_window = init_precision_window() # initialize
        precision_cnt += 1
    ########################### one pass
    print("removed {} in loop {}".format(rmv_cnt,k))




note_list = [to_pattern(beat[0],beat[1]) for beat in beat_list_lane]

#note_list = [to_pattern(note_to_lane(beat[0]),beat[1]) for beat in beat_list]

if VERBOSE:
    print("NOTE list: ",note_list)



print("len of NOTE list: ",len(note_list))




result = '{},213,6,{},120\n'.format(TOTAL_AUDIO_LEN,len(note_list))

for note_info in note_list:
    result += note_info

if VERBOSE:
    print(result)

# write chart

with open("%s" % full_path, "w") as f:
    f.write(result)



'''
