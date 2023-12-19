'''
Collection of functions which draws stuff on screen

'''

import pygame
from variables import *
import os, sys

'''
When player clickes appropriate keys, 
computer highlights pressed 'line'
'''

IMAGE_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))+'/images/'


def load_image(filename):
    APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))+'/images/'
    full_path = os.path.join(APP_FOLDER, '%s.PNG'%filename)
    return pygame.image.load(full_path)


def highlight_line(screen, line_no):
    image = load_image('highlight')
    adjusting_factor = 50 #100
    above_judgement_line = judgement_line_depth
    screen.blit(image, (line_width*line_no, judgement_line- adjusting_factor-above_judgement_line), (0, -adjusting_factor, line_width, judgement_line_depth+adjusting_factor))
    # print("Pressed: %dth line"%line_no)


def draw_arrow(filename,screen,x,y):
    image = load_image(filename)
    screen.blit(image, (x -image.get_width() // 2, y - image.get_height() // 2))


def draw_bar(screen,x,y,bar_width,bar_height, current_percent, color): # x,y is a position of x,y axis of bar
    pygame.draw.rect(screen,color,[x-bar_width//2, y-bar_height//2,int(bar_width*(current_percent/100)),bar_height])

def draw_bar_frame(screen,x,y,bar_width,bar_height, color):
    frame_line_width = 4
    pygame.draw.line(screen, color, [x-bar_width//2, y-bar_height//2], [x-bar_width//2, y+bar_height//2], frame_line_width)
    pygame.draw.line(screen, color, [x+bar_width//2, y-bar_height//2], [x+bar_width//2, y+bar_height//2], frame_line_width)

    pygame.draw.line(screen, color, [x-bar_width//2, y-bar_height//2], [x+bar_width//2, y-bar_height//2], frame_line_width)
    pygame.draw.line(screen, color, [x-bar_width//2, y+bar_height//2], [x+bar_width//2, y+bar_height//2], frame_line_width)
