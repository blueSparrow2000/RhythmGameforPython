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

    return song_bpm, song_length, song_difficulty, total_points

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

        lines = lines[1:]

        for line in lines:
            line.rstrip()
            data = line.split(',')
            if data[0] == 'node':
                node_request = [data[0] ,int(data[1]),int(data[2]),int(data[3])]
                request.append(node_request)
            elif data[0] == 'hold':
                hold_request = [data[0] ,int(data[1]),int(data[2]),int(data[3]),int(data[4])]
                request.append(hold_request)
            else:
                print("Error: Un-identified node type in the given file.")
                break

    print("Current song: %s"%song_name)
    print("BPM: %d" %  song_bpm)
    print("Total Points: %d"%total_points)
    print("Difficulty: %d" %  song_difficulty)

    return total_points,song_difficulty,song_length, song_bpm,request
