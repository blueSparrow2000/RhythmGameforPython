'''
Reads files which has information of chart
which includes:
(time offset in milliseconds, line number)


Update: hold node is included, then change to
node:
(node type, time offset in milliseconds, line number,points)

hold:
(node type, time offset in milliseconds, line number, points, length)

'''

import pygame
import os, sys
from chart_builder import *

def get_chart_info(song_name):
    APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))+'/charts/'
    full_path = os.path.join(APP_FOLDER, '%s.txt'%song_name)

    with open("%s"%full_path, "r") as f:
        lines = f.readlines()
        first_line = lines[0]
        first_line.rstrip()
        first_line = first_line.split(',')
        song_length = int(first_line[0])
        song_bpm = int(first_line[1])  # milli-seconds per beat
        song_difficulty = int(first_line[2])
        total_points = int(first_line[3])
        recommended_fps = int(first_line[4])

    return song_bpm, song_length, song_difficulty, total_points, recommended_fps

def get_chart(song_name):
    APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))+'/charts/'
    full_path = os.path.join(APP_FOLDER, '%s.txt'%song_name)

    request = []

    with open("%s"%full_path, "r") as f:
        lines = f.readlines()
        first_line = lines[0]
        first_line.rstrip()
        first_line = first_line.split(',')
        song_length = int(first_line[0])
        song_bpm = int(first_line[1])  # milli-seconds per beat
        song_difficulty = int(first_line[2])
        total_points = int(first_line[3])
        recommended_fps = int(first_line[4])

        lines = lines[1:]

        for line in lines:
            line.rstrip()
            data = line.split(',')

            request.append(data) # just feed a raw information


    print("Current song: %s"%song_name)
    print("BPM: %d" %song_bpm)
    print("Total Points: %d"%total_points)
    print("Difficulty: %d"%song_difficulty)
    print("Recommended_fps: %d"%recommended_fps)

    return total_points, song_difficulty, song_length, song_bpm, recommended_fps, request
