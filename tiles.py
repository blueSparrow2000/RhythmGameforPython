'''
Nodes, holds, arcs

'''

import pygame
from variables import *
from text_writer import *
import math

class Node():
    def __init__(self,line,point):
        self.name = 'node'
        self.y = node_spawning_y_pos
        self.line = line # 몇 번 line에 넣을지 결정
        self.color = (180,180,180)
        self.point = point

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,[line_axes[self.line-1]-line_width//2,self.y-node_height//2,line_width,node_height])

    def move(self,speed):
        self.y += (speed*10/fps)

    def check_border(self):
        if self.y >= height: # then node arrived at the border!
            #print("Border!")
            return True
        else:
            return False

class Hold():
    def __init__(self,line,point,length):
        self.name = 'hold'
        self.y = node_spawning_y_pos  # hold 노드의 y 값은 제일 아래쪽의 y좌표이다. 즉, 홀드 노드의 시작점 좌표!
        self.length = length
        self.tail = self.y-self.length

        self.holding = False  # 자신이 눌러지고 있는지 판단

        self.line = line # 몇 번 line에 넣을지 결정
        self.not_holding_color = (140,140,140)
        self.holding_color = (210,210,210)
        self.color = self.not_holding_color
        self.point = point

        self.this_judgement_pos = node_spawning_y_pos

    def draw(self,screen):
        pygame.draw.rect(screen,self.color ,[line_axes[self.line-1]-line_width//2,max(self.y-self.length,info_length),line_width,min(self.length,self.y-info_length)])

    def update_color(self):
        if self.holding:
            self.color = self.holding_color
        else:
            self.color = self.not_holding_color

    def move(self,speed):
        increment = (speed*10/fps)
        self.y += increment
        self.this_judgement_pos += increment
        self.tail = self.y - self.length

    def check_border(self):
        if self.tail>= height: # then node arrived at the border!
            #print("Border!")
            return True
        else:
            return False
