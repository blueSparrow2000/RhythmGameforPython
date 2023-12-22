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
    def __init__(self,stage_speed,offset,screen,request_list,song_name,song_bpm, given_fps, beat_line_request = False):
        global song_offsets
        self.screen = screen
        self.speed = stage_speed # pixel per 100 millisecond (node speed x == x*10 pixel/second)

        if song_name in song_offsets.keys():
            song_offset = song_offsets[song_name]
        else:
            song_offset = 0
        self.offset = offset + int(offset_corresponding_to_speed(self.speed)) + song_offset
        print("Offset: ",self.offset)
        self.delta_t = ((line_length - node_spawning_y_pos)/self.speed)*100 # (millisecond)

        self.given_fps = given_fps
        self.fps_error = (1000//self.given_fps) # in milliseconds

        ############### enhance distributer speed ##################
        # modify request string in advance
        tile_requests = []
        '''
        request[0] string: pattern (N___ etc.)
        request[1] string: beat position (ms)
        request[2,3,4,5] string: infos either '' or string separated by '/' 
        '''
        for request in request_list:
            tile_pattern = request[0]
            beat_pos_of_current_request = int(request[1])
            nodes_to_to_append_at_current_request = []
            holdes_to_to_append_at_current_request = []

            if len(tile_pattern) != 4:
                raise ValueError("Tile pattern not given as length-4 string!")

            for i in range(4):  # there are 4 lines so go through 4 lines
                if tile_pattern[i] == '_':
                    continue
                tile_info = request[2 + i].split('/')  # specific info are separated by '/'

                # print(i+1,tile_info)

                if tile_pattern[i] == 'N':
                    # create node
                    n = Node(i + 1, int(tile_info[0]), self.given_fps, tile_info[1].strip())
                    # note that from now we have to write all nodes 'special' attribute (like normal)!

                    # distribute the node on the screen
                    nodes_to_to_append_at_current_request.append(n)
                elif tile_pattern[i] == 'H':
                    # create hold
                    length = int(tile_info[1]) * self.speed // 100
                    h = Hold(i + 1, int(tile_info[0]), length, self.given_fps, tile_info[2].strip())
                    # distribute the hold on the screen
                    holdes_to_to_append_at_current_request.append(h)

            tile_requests.append( [beat_pos_of_current_request, nodes_to_to_append_at_current_request, holdes_to_to_append_at_current_request] )

        ############################################################
        #print(len(tile_requests))
        self.tile_requests = tile_requests
        self.beat_line_request = beat_line_request
        self.song_mpb = ((1000 * 60 / song_bpm))

        self.distributer_creation_time = pygame.time.get_ticks() #+ correction # distributer가 만들어진 이후 지나간 시간 (외부에서 '진짜'음악이 시작한 시각은 다름)

        # variables related to music starting timing issue
        self.ready = False
        first_request = self.tile_requests[0]

        self.very_first_request_deploy_time = - self.delta_t
        self.first_request_time_respect_to_music_start = int(first_request[0])

        self.first_call = True

        self.music_did_start_right_away = False
        self.state_determined = False

        # 시간 보정
        self.time_anomaly = 0



    def print_next_n_requests(self,num):
        # print first 10 nodes
        print('='*50)
        ind = 0
        while ind<min(len(self.tile_requests),num):
            print(self.tile_requests[ind])
            ind+=1

    def get_time(self): # distributer가 만들어진 후 경과한 시간
        time = pygame.time.get_ticks() - self.distributer_creation_time
        return time

    def distribute(self,nodes_on_screen,holds_on_screen,beat_lines):
        cur_time = self.get_time()  # deployer 시작 후 경과한 시간

        if self.first_call: # initialize distributer when called first time
            if cur_time != 0:
                self.distributer_creation_time = pygame.time.get_ticks()
                cur_time = 0
                self.first_call = False

        if self.beat_line_request and self.deploy_time(int(cur_time%self.song_mpb),0):
            #print(cur_time%self.song_mpb)
            self.deploy_beat_line(cur_time, beat_lines)
            #pass

        # ready check
        if not self.ready:
            # check whether first node deploy time is negative ==> not ready (deployer가 만들어진 후
            if not self.state_determined and cur_time > -self.very_first_request_deploy_time:  # ready하기 전에 한번이라도 이런 적이 있으면
                self.music_did_start_right_away = True
                self.state_determined = True
            if cur_time >= -self.very_first_request_deploy_time:
                self.ready = True

        cur_time = cur_time - (self.offset + self.time_anomaly)


        if not self.tile_requests == []:  # if request is not empty, deploy nodes!
            current_request = self.tile_requests[0]
            current_request_deploy_time = int(current_request[0])
            #print("music did start right away")

            # precise한 정도를 조절. 1이 미니멈
            if not self.deploy_time(current_request_deploy_time,cur_time): #> self.fps_error//2:
                return

            while self.deploy_time(current_request_deploy_time,cur_time): #<= self.fps_error//2: # 해당 노드가 소환되어야 할 시점을 지나면
                tile_pattern = current_request[0]
                nodes_to_add = current_request[1]
                holds_to_add = current_request[2]
                for node in nodes_to_add:
                    nodes_on_screen.append(node)
                for hold in holds_to_add:
                    holds_on_screen.append(hold)

                self.tile_requests.remove(current_request)

                # next step
                if self.tile_requests == []: # if empty
                    break
                current_request = self.tile_requests[0]
                current_request_deploy_time = int(current_request[0]) - self.delta_t

                #print(nodes_on_screen)
                #print(holds_on_screen)
                #print("="*30)

    def multi_tile_translator(self,tile_pattern):
        # N is node, H is hold, _ is empty
        return


    def deploy_time(self,first_deploy_time,cur_time):
        return abs(first_deploy_time-cur_time) <= self.fps_error #or first_deploy_time<=cur_time

    def near_passed_deploy_time(self,first_deploy_time,cur_time):
        return 0 <= cur_time - first_deploy_time <= 50

    def node_not_deployed(self,node):
        pass

    def deploy_beat_line(self,cur_time,beat_lines):
        # print(cur_beat_time," 비트타임\n보정 시간: ",cur_time+(self.offset + self.time_anomaly))
        beat_lines.append(BeatLine(cur_time//self.song_mpb,self.given_fps ,show_beat = False))
        #print("Deployed!")

