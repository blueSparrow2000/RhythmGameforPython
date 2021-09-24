'''
Music file handling

check these:
https://stackoverflow.com/questions/65856144/check-whether-a-song-has-finished-playing-in-pygame
https://stackoverflow.com/questions/65869913/how-to-get-out-of-the-while-loop-in-pygame-when-after-playing-the-music
'''

import pygame
import os, sys
from variables import *

mixer_channel_num = 8  # default 로 8임
MUSIC_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))+'/cc_musics/'

# music은 stage와 main에서만 튼다
def music_Q(music_file,repeat = False): #현재 재생되고 있는 음악을 확인하고 음악을 틀거나 말거나 결정해야 할때 check_playing_sound = True 로 줘야 함
    global MUSIC_FOLDER
    full_path = os.path.join(MUSIC_FOLDER, '%s.mp3'%music_file)

    pygame.mixer.init()
    pygame.mixer.music.load(full_path)
    song_start_time = 0 # adjust start times of the songs if needed...
    pygame.mixer.music.set_volume(0.06)

    # if music_file == 'Sugar':
    #     pygame.mixer.music.set_volume(0.04)
    #     song_start_time = 0
    if repeat:
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.play()

    return song_start_time # returns start time! (in milliseconds)

def get_musics():
    global MUSIC_FOLDER
    full_path = os.path.join(MUSIC_FOLDER, 'music_list.txt')
    list_ = []
    #print("%s"%full_path)
    with open("%s"%full_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            list_.append(line.strip())
    return list_

def get_music_info(song_name):
    APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))+'/CC_musics/'
    full_path = os.path.join(APP_FOLDER, '%s.txt'%song_name)

    with open("%s"%full_path, "r") as f:
        credit = f.readlines()
        print(credit)
        max_len = 60
        for i in range(len(credit)):
            line = credit[i].strip()
            cnt = 0
            del credit[i]
            while len(line) > max_len:
                shortened_front = line[:max_len]
                credit.insert(i+cnt,shortened_front)
                line = line[max_len:]
                cnt+=1
                #print(i+cnt)
            credit.insert(i + cnt, line)
    #print(credit)
    return credit

def add_musics():
    music_name = input('Enter music name: ')
    full_path = os.path.join(MUSIC_FOLDER, 'music_list.txt')

    with open("%s"%full_path, "a") as f:
        f.write(music_name+'\n')

def check_music_exists():
    pass

def check_music_ended(song_start_time):
    #print(song_start_time)
    if song_start_time == -1: # not started
        return False
    # return True if music is still going. returns False if music is paused or ended.
    return not pygame.mixer.music.get_busy()