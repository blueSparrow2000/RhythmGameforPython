'''
Distributer

분배기 - 차트에서 읽어들인 노트를 게임에 분배함

* Note: distributer's accuracy depends on song_mbps!
So be sure to write in the correct value for song_bps (in each chart builder)!
(or if you want precision, you may increase song_bps i.e, double the bps)
'''


import pygame
from variables import *
from text_writer import *
from tiles import *
import math
from frame_class import *


def func1(input):
    return -0.3835*(input**2)+53.213*input-315.61

def func2(input):
    return 183.37*math.log(input)+56.319

def offset_corresponding_to_speed(input):
    if 10<=input<=20:
        return func1(input)
    elif 20<input<=100:
        return func2(input)
    else:
        return 0 # no offset info


class Distributer():
    def __init__(self,stage_speed,offset,screen,request,song_name,song_bpm,beat_line_request = False):
        global fps, song_offsets
        self.screen = screen
        self.speed = stage_speed # pixel per 100 millisecond (node speed x == x*10 pixel/second)
        #self.speed_offsets = {10:180,20:600,50:790,80:850}
        if song_name in song_offsets.keys():
            song_offset = song_offsets[song_name]
        else:
            song_offset = 0
        self.offset = offset + int(offset_corresponding_to_speed(self.speed)) + song_offset#self.speed_offsets[self.speed]  #180+(self.speed-10)*(720/70) #self.speed_offsets[self.speed] #770#+ (80 - self.speed)*11
        print("Offset: ",self.offset)
        self.delta_t = ((line_length - node_spawning_y_pos)/self.speed)*100 # (millisecond)
        self.fps_error = (1000//fps) # in milliseconds

        self.request =  request
        self.beat_line_request = beat_line_request
        self.song_mpb = ((1000 * 60 / song_bpm))


        #correction= 220 # distributer의 초기 시작값이 0이 아닌 220이 나와서 필요한 인자
        self.distributer_creation_time = pygame.time.get_ticks() #+ correction # distributer가 만들어진 이후 지나간 시간 (외부에서 '진짜'음악이 시작한 시각은 다름)

        # variables related to music starting timing issue
        self.ready = False
        first_node = self.request[0]

        self.very_first_node_deploy_time = - self.delta_t #first_node[1] - self.delta_t
        self.first_node_time_respect_to_music_start = first_node[1]

        self.first_call = True

        self.music_did_start_right_away = False
        self.state_determined = False

        # 시간 보정
        self.time_anomaly = 0

        # print first 10 nodes
        # num = 10
        # ind = 0
        # while ind<min(len(self.request),num):
        #     print(self.request[ind])
        #     ind+=1

    def print_next_n_requests(self,num):
        # print first 10 nodes
        print('='*50)
        ind = 0
        while ind<min(len(self.request),num):
            print(self.request[ind])
            ind+=1

    def get_time(self): # distributer가 만들어진 후 경과한 시간
        time = pygame.time.get_ticks() - self.distributer_creation_time
        return time

    # def deploy_beat_line(self, song_bpm, beat_lines):
    #     pass

    def distribute(self,nodes_on_screen,holds_on_screen,beat_lines):
        cur_time = self.get_time()  # deployer 시작 후 경과한 시간
        if self.first_call:
            if cur_time != 0:
                self.distributer_creation_time = pygame.time.get_ticks()
                cur_time = 0
                self.first_call = False
        # distributer가 distribute()를 불렀을 때 직후의 시간!
        #print(cur_time)

        if self.beat_line_request and self.deploy_time(int(cur_time%self.song_mpb),0):
            #print(cur_time%self.song_mpb)
            self.deploy_beat_line(cur_time, beat_lines)
            #pass

        # ready check
        if not self.ready:
            # check whether first node deploy time is negative ==> not ready (deployer가 만들어진 후
            if not self.state_determined and cur_time > -self.very_first_node_deploy_time:  # ready하기 전에 한번이라도 이런 적이 있으면
                self.music_did_start_right_away = True
                self.state_determined = True
            if cur_time >= -self.very_first_node_deploy_time:
                self.ready = True
                # print("music start time: ",cur_time)
                # print('='*100)
                # self.print_next_n_requests(3)
                #print(self.very_first_node_deploy_time - cur_time)
        # if self.ready:
        #     print("Time after music start ",cur_time)

        cur_time = cur_time - (self.offset + self.time_anomaly)

        if not self.request == []:  # if request is not empty, deploy nodes!
            first_node = self.request[0]
            # first_node_deploy_time = first_node[
            #                              1] - self.first_node_time_respect_to_music_start # 노드가 소환되어야 하는 시각 (music이 틀어진 시점을 0로 볼때)
            #first_node[1] 는 music이 시작되고 나서 노드가 내려오는 시각!
            first_node_deploy_time = first_node[1]#self.first_node_time_respect_to_music_start # 노드가 소환되어야 하는 시각 (music이 틀어진 시점을 0로 볼때)
            #print("music did start right away")

            # if cur_time%16 == cur_time%(16*16):
                #print("next node deploy time: ",first_node_deploy_time)
                #self.print_next_n_requests(3)
                # print(cur_time)
            # if self.near_passed_deploy_time(first_node_deploy_time, cur_time):
            #     print(cur_time)
            #     print("Passed ", first_node_deploy_time)

            # precise한 정도를 조절. 1이 미니멈
            if not self.deploy_time(first_node_deploy_time,cur_time): #> self.fps_error//2:
                # print(first_node_deploy_time)
                return
            #loop_cnt = 0
            while self.deploy_time(first_node_deploy_time,cur_time): #<= self.fps_error//2: # 해당 노드가 소환되어야 할 시점을 지나면
                #print('Correct loop')
                if first_node[0] == 'node':
                    n = Node(first_node[2],first_node[3])
                    # print("cur time: ",cur_time)
                    # print("deploy error: ",first_node_deploy_time-cur_time)
                    # print("removed node at time: ", first_node_deploy_time)
                    self.request.remove(first_node)
                    nodes_on_screen.append(n)

                    #print(loop_cnt)
                elif first_node[0] == 'hold':
                    length = first_node[4]*self.speed//100
                    n = Hold(first_node[2],first_node[3],length)
                    self.request.remove(first_node)
                    holds_on_screen.append(n)
                #self.time_anomaly += first_node_deploy_time-cur_time
                # next step
                if self.request == []: # if empty
                    break
                first_node = self.request[0]
                first_node_deploy_time = first_node[1] - self.delta_t
                #loop_cnt+=1


    def deploy_time(self,first_deploy_time,cur_time):
        return abs(first_deploy_time-cur_time) <= self.fps_error #or first_deploy_time<=cur_time

    def near_passed_deploy_time(self,first_deploy_time,cur_time):
        return 0 <= cur_time - first_deploy_time <= 50

    def node_not_deployed(self,node):
        pass

    def deploy_beat_line(self,cur_time,beat_lines):
        # print(cur_beat_time," 비트타임\n보정 시간: ",cur_time+(self.offset + self.time_anomaly))
        beat_lines.append(BeatLine(cur_time//self.song_mpb,show_beat = False))
        #print("Deployed!")

