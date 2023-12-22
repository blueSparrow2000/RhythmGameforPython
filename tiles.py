'''
Nodes, holds, arcs

'''

import pygame
from variables import *
from text_writer import *
import math

class Node():
    def __init__(self,line,point,given_fps, special = None):
        global judgement_line, height, node_color ,bad_apple_toggled_color,bad_apple_color,debug_color,change_background_color
        self.given_fps = given_fps

        self.judgement_line = judgement_line
        self.height = height

        self.name = 'node'
        self.y = node_spawning_y_pos
        self.line = line # 몇 번 line에 넣을지 결정

        self.node_color =  node_color
        self.color = node_color[change_background_color[0]] #node_color
        self.bad_apple_toggled_color = bad_apple_toggled_color
        self.bad_apple_color = bad_apple_color
        self.debug_color = debug_color

        self.point = point

        if special == '': # replace it to None object
            special = None

        self.special = special # special node

    def draw(self, screen, screen_freeze = False):
        if self.special == 'BadApple':
            if screen_freeze: # at screen freeze
                pygame.draw.rect(screen, self.bad_apple_toggled_color,
                                 [line_axes[self.line - 1] - line_width // 2, self.y - node_height // 2, line_width,
                                  node_height])
            else:  # no screen freeze
                pygame.draw.rect(screen, self.bad_apple_color,
                                 [line_axes[self.line - 1] - line_width // 2, self.y - node_height // 2, line_width,
                                  node_height])
        elif self.special == 'Debug':
            pygame.draw.rect(screen, self.debug_color,
                             [line_axes[self.line - 1] - line_width // 2, self.y - node_height // 2, line_width,
                              node_height])
        else:
            pygame.draw.rect(screen, self.node_color[change_background_color[0]],
                             [line_axes[self.line - 1] - line_width // 2, self.y - node_height // 2, line_width,
                              node_height])

    def move(self,speed):
        self.y += (speed*10/self.given_fps)

    def fix_loc(self, loc = None):
        if loc:
            self.y = loc
        else:
            self.y = self.judgement_line

    def check_border(self):
        if self.special == 'BadApple' and self.y > self.judgement_line + 5:  # 'Late' for special node
            #print('border cross for Bad apple!')
            return True # border crossed for special node
        if creater_mode:
            if self.y >= self.judgement_line: #self.height: # then node arrived at the border!
                #print("Border!")
                return True
            else:
                return False
        else:
            if self.y >= self.height: # then node arrived at the border!
                #print("Border!")
                return True
            else:
                return False


    def special_effect(self):
        if self.special=='BadApple':
            return 'wait'

    def freeze(self):
        self.color = self.node_color[change_background_color[0]]


class Hold():
    def __init__(self,line,point,length,given_fps,special=None):
        global judgement_line, height, hold_color, holding_middle_color , not_holding_color,not_holding_middle_color, debug_color,change_background_color
        self.given_fps = given_fps

        self.judgement_line = judgement_line
        self.height = height

        self.name = 'hold'
        self.y = node_spawning_y_pos  # hold 노드의 y 값은 제일 아래쪽의 y좌표이다. 즉, 홀드 노드의 시작점 좌표!
        self.length = length
        self.tail = self.y-self.length

        self.holding = False  # 자신이 눌러지고 있는지 판단

        self.line = line # 몇 번 line에 넣을지 결정
        self.debug_color = debug_color
        self.not_holding_middle_color = not_holding_middle_color
        self.holding_middle_color = holding_middle_color

        self.color = hold_color[change_background_color[0]] #self.not_holding_color
        self.middle_color = not_holding_middle_color

        self.hold_color = hold_color

        self.point = point

        self.this_judgement_pos = node_spawning_y_pos

        if special == '': # replace it to None object
            special = None

        self.special = special # special node

    def draw(self,screen,screen_update = True):
        if self.special == 'Debug':
            pygame.draw.rect(screen,self.debug_color ,[line_axes[self.line-1]-line_width//2,max(self.y-self.length,info_length),line_width,min(self.length,self.y-info_length)])
        else:
            pygame.draw.rect(screen,self.hold_color[change_background_color[0]],[line_axes[self.line-1]-line_width//2,max(self.y-self.length,info_length),line_width,min(self.length,self.y-info_length)])
            pygame.draw.rect(screen,self.middle_color ,[line_axes[self.line-1]-line_width//16,max(self.y-self.length,info_length),line_width//8,min(self.length,self.y-info_length)])


    def update_color(self):
        if self.holding:
            self.middle_color = self.holding_middle_color
        else:
            self.middle_color = self.not_holding_middle_color

    def move(self,speed):
        increment = (speed*10/self.given_fps)
        self.y += increment
        self.this_judgement_pos += increment
        self.tail = self.y - self.length

    def fix_loc(self, loc = None):
        if loc:
            self.y = loc
        else:
            self.y = self.judgement_line

    def check_border(self):
        if self.tail>= self.height: # then node arrived at the border!
            #print("Border!")
            return True
        else:
            return False


    def special_effect(self,screen):
        pass

    def freeze(self):
        self.color = self.hold_color[change_background_color[0]]
