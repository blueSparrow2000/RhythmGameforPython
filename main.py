'''
Main loop

Rythm game version 1.0 released!
- Currently one song available but you can add songs and choose them
- Currently one chart available



- offset/speed adjustments


Tile types
- node: press F,G,H,J at appropriate time
- hold: keep pressing F,G,H,J until hold ends. It will keep check whether player is holding itself at regularly selected time


'''

import pygame
from variables import *
from utility_functions import *
from music_ import *
from text_writer import *
from image_processor import *
from chart import *
from screen_options import *
from song_selection import *


pygame.init()  # 파이게임 초기화
clock = pygame.time.Clock()
# computer screen size: 1920 x 1080

screen = pygame.display.set_mode((width, height))  # window 생성
pygame.display.set_caption('Rythm Game')  # window title
width, height = pygame.display.get_surface().get_size()  # window width, height

screen.fill(background_color[0])  # background color

# main screen ---------------------------------------------------
run = True
meta_run = True

def exit():
    pygame.quit()
    return False, False

while meta_run:
    global stage_speed, offset, judgement_shown, guide_line_shown, high_quality_verifying_graphics, music_list, music_pointer, song_name
    # The Music in main
    music_Q(lobbyMusic,True)
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 윈도우를 닫으면 종료
                run, meta_run = exit()
                break

            if event.type == pygame.MOUSEMOTION:
                # player가 마우스를 따라가도록
                # point.pos = pygame.mouse.get_pos()
                pass

            if event.type == pygame.MOUSEBUTTONUP:
                (xp, yp) = pygame.mouse.get_pos()
                mouse_particle_list.append((pygame.time.get_ticks(),(xp, yp)))
                mouse_click_sound()

                if abs(xp - option_key_x_level) < big_text*6:
                    if abs(yp - (option_key_y_level)) < big_text:
                        print('option clicked!')
                        run = False
                        stage_speed, offset, judgement_shown, guide_line_shown, high_quality_verifying_graphics = option_screen(screen,clock,stage_speed, offset, judgement_shown, guide_line_shown, high_quality_verifying_graphics)
                        #print(stage_speed, offset, judgement_shown, guide_line_shown, high_quality_verifying_graphics)
                        break

                if abs(xp - song_selection_key_x_level) < big_text*6:
                    if abs(yp - (song_selection_key_y_level)) < big_text:
                        print('song selection clicked!')
                        run = False
                        music_list, music_pointer, song_name = song_selection_screen(screen,clock,stage_speed, offset, judgement_shown, guide_line_shown, high_quality_verifying_graphics)
                        #print(music_list, music_pointer, song_name)
                        break



            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # esc 키를 누르면 종료
                    run, meta_run = exit()
                    break

                elif event.key == pygame.K_RETURN:
                    print('Going to song selection!')
                    run = False
                    music_list, music_pointer, song_name = song_selection_screen(screen, clock, stage_speed, offset,
                                                                                 judgement_shown, guide_line_shown,
                                                                                 high_quality_verifying_graphics)
                    break



        if not run:
            break

        screen.fill(background_color[0])

        if creater_mode:
            write_text(screen, width // 2, small_text*2, '- This is a creater mode -', small_text, background_color[0],
                       debug_color)

        write_text(screen, width//2, height//8 , 'A rhythm game in pygame', big_text, background_color[0], highlight_text_color)

        write_text(screen, option_key_x_level, option_key_y_level,
                   'Options', big_text, background_color[0],
                   highlight_text_color)
        pygame.draw.rect(screen, highlight_text_color, [width//4 - big_text, option_key_y_level - button_y_offset, button_x_size, button_y_size], 4,8)

        write_text(screen, song_selection_key_x_level, song_selection_key_y_level,
                   'Song selection', big_text, background_color[0],
                   highlight_text_color)
        pygame.draw.rect(screen, highlight_text_color, [width//4 - big_text,  song_selection_key_y_level - button_y_offset, button_x_size, button_y_size], 4,8)

        write_text(screen, width // 2, height-small_text*4, 'How to play: ', small_text, background_color[0],
                   highlight_text_color)
        write_text(screen, width // 2, height-small_text*2, 'press %s,%s,%s,%s in appropriate timing!'%(guide_keys[0],guide_keys[1],guide_keys[2],guide_keys[3]), small_text, background_color[0],
                   highlight_text_color)

        if mouse_particle_list:  # if not empty
            #print(len(mouse_particle_list))
            current_run_time = pygame.time.get_ticks()
            for mouse_particle in mouse_particle_list:
                #draw_particle(screen, mouse_particle)
                mouse_click_time = mouse_particle[0]
                position = mouse_particle[1]
                delta = (current_run_time - (mouse_click_time))/1000
                if  delta >= water_draw_time_mouse:
                    mouse_particle_list.remove(mouse_particle)
                factor = delta / water_draw_time_mouse
                radi = calc_drop_radius(factor, mouse_particle_radius)
                pygame.draw.circle(screen,effect_color, position, radi, particle_width_mouse)



        pygame.display.flip()
        clock.tick(main_loop_render_fps)

