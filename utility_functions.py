'''
some useful functions!

'''
import math
import pygame

mouse_particle_list = []  # mouse click effects
water_draw_time = 0.8
water_draw_time_mouse = 0.6
particle_width = 6
particle_width_mouse = 3
mouse_particle_radius = 5
droplet_radius = 33
effect_color = (150, 200, 240)

def boundary_checker(min_,max_,value):
    if value>max_:
        value = max_
    elif value<min_:
        value = min_
    return value

# def show_grades(screen):
#     cnt = 0
#     for score_color in score_colors.keys():
#         write_text(screen, width // 2, (height // 5) * 4 + small_text * cnt, '%s' % (score_color), small_text,
#                    background_color[0],
#                    score_colors[score_color])
#         cnt += 1


def calc_drop_radius(factor,start_radius,mouse=True):  # factor is given by float between 0 and 1 (factor changes from 0 to 1)
    if not mouse:
        width = int(math.pow(3*(1-factor),3)+3.5)
    else:
        width = int(math.pow(2.5*(1-factor),3)+1.7)
    r = max(width,int(start_radius*(1+4*math.pow(factor,1/5))))
    return r

def color_safe(color):
    color = int(color)
    return max(0,min(color,255))

def millisecond_pixel_converter(m,speed):
    return int(m*speed/100)