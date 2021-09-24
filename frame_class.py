import pygame
from variables import *
from text_writer import *
import math


class BeatLine():
    def __init__(self,cur_beat_time,show_beat = False):
        self.name = 'beat line'
        self.y = node_spawning_y_pos
        self.cur_beat_time = cur_beat_time
        self.show_beat = show_beat
        self.color = (80,80,80)
        self.width = 2

    def draw(self,screen):
        if self.show_beat:
            write_text(screen, width//2, self.y-small_text, '%s'%self.cur_beat_time, small_text, background_color[0], self.color)
        pygame.draw.line(screen, judgement_line_color, [0, self.y],
                         [width, self.y], self.width)

    def move(self,speed):
        self.y += (speed*10/fps)

    def check_border(self,beat_list):
        if self.y >= height: # then node arrived at the border!
            beat_list.remove(self)
        else:
            pass
