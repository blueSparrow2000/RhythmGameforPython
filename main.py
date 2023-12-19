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
from game import *
from music_ import *
from text_writer import *
from image_processor import *

pygame.init()  # 파이게임 초기화
clock = pygame.time.Clock()
# computer screen size: 1920 x 1080

screen = pygame.display.set_mode((width, height))  # window 생성
pygame.display.set_caption('Rythm Game')  # window title
width, height = pygame.display.get_surface().get_size()  # window width, height

screen.fill(background_color[0])  # background color

# main screen ---------------------------------------------------
# default settings - mode는 stage에서 바꾼다!
mode = 'Play'

character ='1'

run = True
meta_run = True

def exit():
    pygame.quit()
    return False, False

def boundary_checker(min_,max_,value):
    if value>max_:
        value = max_
    elif value<min_:
        value = min_
    return value

def show_grades(screen):
    cnt = 0
    for score_color in score_colors.keys():
        write_text(screen, width // 2, (height // 5) * 4 + small_text * cnt, '%s' % (score_color), small_text,
                   background_color[0],
                   score_colors[score_color])
        cnt += 1


def update_song_info():
    global song_info_list
    new_song_name = music_list[music_pointer]
    song_info_list = list(get_chart_info(new_song_name))
    return new_song_name

while meta_run:
    # The Music in main
    music_Q(lobbyMusic,True)
    run = True
    global music_list, music_pointer, song_name
    music_list = get_musics()

    number_of_musics = len(music_list)

    min_index = max(music_pointer - 2, 0)
    max_index = min(music_pointer + 2, number_of_musics - 1)

    song_name = music_list[music_pointer]
    song_name = update_song_info()

    mode_y_level =  height // 3
    offset_x_level = (width//7)*2
    # {'[mode name]':([mode location offset on screen], [value of adjustment])}
    mode_location_offset = {'Giant':big_text*4,'huge':big_text*3+small_text,'big':big_text*2+small_text,'small':big_text}

    offset_mode = {'10up':(-mode_location_offset['big'],10), '1up':(-mode_location_offset['small'],1),'10down':(mode_location_offset['big'],-10), '1down':(mode_location_offset['small'],-1)}
    offset_mode_keys = offset_mode.keys()

    speed_x_level = (width//7)*5
    speed_mode = {'10up':(-mode_location_offset['big'],10), '1up':(-mode_location_offset['small'],1),'10down':(mode_location_offset['big'],-10), '1down':(mode_location_offset['small'],-1)}
    speed_mode_keys = speed_mode.keys()


    song_list_x_level = 3 * (width // 10)

    song_info_x_level = 7*(width // 10)
    song_info_y_level = (height // 8) * 6
    song_info_big_step = 10
    song_info_small_step = 5


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

                if abs(xp - offset_x_level) < big_text*2:
                    for offset_ in offset_mode_keys:
                        if abs(yp - (mode_y_level+offset_mode[offset_][0])) < big_text//2:
                            offset += offset_mode[offset_][1]*10
                            offset = boundary_checker(min_offset,max_offset,offset)

                if abs(xp - speed_x_level) < big_text*2:
                    for speed_ in speed_mode_keys:
                        if abs(yp - (mode_y_level+speed_mode[speed_][0])) < big_text//2:
                            stage_speed += speed_mode[speed_][1]
                            stage_speed = boundary_checker(min_speed,max_speed,stage_speed)

                if abs(xp - width//2) < big_text*3:  # toggle judgement
                    if abs(yp - (mode_y_level + mode_location_offset['huge'] + big_text + big_text//2))< big_text//2:
                        judgement_shown = not judgement_shown #not judgement_shown

                if abs(xp - width//2) < big_text*3:  # toggle guide line
                    if abs(yp - (mode_y_level + mode_location_offset['huge'] + big_text*2 + big_text//2))< big_text//2:
                        guide_line_shown = not guide_line_shown

                if abs(xp - width // 2) < big_text * 3:  # toggle graphics
                    if abs(yp - (mode_y_level + mode_location_offset['huge'] + big_text * 3 + big_text//2)) < big_text // 2:
                        high_quality_verifying_graphics = not high_quality_verifying_graphics


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    music_pointer -= 1
                    music_pointer = boundary_checker(0,number_of_musics-1,music_pointer)
                    # 이 연산은 music pointer가 바뀌었을때만 하면 된다
                    min_index = max(music_pointer - 2, 0)
                    max_index = min(music_pointer + 2, number_of_musics - 1)
                    song_name = update_song_info()

                if event.button == 5:
                    music_pointer += 1
                    music_pointer  = boundary_checker(0,number_of_musics-1,music_pointer)
                    # 이 연산은 music pointer가 바뀌었을때만 하면 된다
                    min_index = max(music_pointer - 2, 0)
                    max_index = min(music_pointer + 2, number_of_musics - 1)
                    song_name = update_song_info()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # esc 키를 누르면 종료
                    run, meta_run = exit()
                    break
                elif event.key == pygame.K_RETURN:
                    run_FGHJ(screen,clock,song_name,stage_speed,offset,judgement_shown,guide_line_shown,high_quality_verifying_graphics)
                    run = False
                    break

                elif event.key == pygame.K_UP:
                    music_pointer -= 1
                    music_pointer = boundary_checker(0,number_of_musics-1,music_pointer)
                    # 이 연산은 music pointer가 바뀌었을때만 하면 된다
                    min_index = max(music_pointer - 2, 0)
                    max_index = min(music_pointer + 2, number_of_musics - 1)
                    song_name = update_song_info()

                elif event.key == pygame.K_DOWN:
                    music_pointer += 1
                    music_pointer = boundary_checker(0, number_of_musics - 1, music_pointer)
                    # 이 연산은 music pointer가 바뀌었을때만 하면 된다
                    min_index = max(music_pointer - 2, 0)
                    max_index = min(music_pointer + 2, number_of_musics - 1)
                    song_name = update_song_info()

        if not run:
            break

        screen.fill(background_color[0])
        write_text(screen, width//2, height//8 , 'Press Enter to play!', big_text, background_color[0], highlight_text_color)

        for offset_ in offset_mode_keys:
            draw_arrow(offset_, screen, offset_x_level, (mode_y_level + offset_mode[offset_][0]))

        write_text(screen, offset_x_level, mode_y_level - mode_location_offset['huge'], 'Late (+)' , tiny_text, background_color[0],
                   highlight_text_color)
        write_text(screen, offset_x_level, mode_y_level + mode_location_offset['huge'], 'Early (-)' , tiny_text, background_color[0],
                   highlight_text_color)

        for speed_ in speed_mode_keys:
            draw_arrow(speed_, screen, speed_x_level, (mode_y_level + speed_mode[speed_][0]))


        #show_grades(screen)

        write_text(screen,  offset_x_level, mode_y_level, 'Offset: %d (ms)'%(offset), small_text, background_color[0],
                   highlight_text_color)
        write_text(screen, speed_x_level, mode_y_level, 'Speed: %d'%(stage_speed), small_text, background_color[0],
                   highlight_text_color)

        if judgement_shown:
            write_text(screen, width // 2,  mode_y_level + mode_location_offset['Giant'] + big_text, 'Judgement detail: On', small_text, background_color[0],
                       highlight_text_color)
        else:
            write_text(screen, width // 2,  mode_y_level + mode_location_offset['Giant'] + big_text, 'Judgement detail: Off', small_text, background_color[0],
                       highlight_text_color)

        if guide_line_shown:
            write_text(screen, width // 2,  mode_y_level + mode_location_offset['Giant'] + big_text*2, 'Guide line: On', small_text, background_color[0],
                       highlight_text_color)
        else:
            write_text(screen, width // 2,  mode_y_level + mode_location_offset['Giant'] + big_text*2, 'Guide line: Off', small_text, background_color[0],
                       highlight_text_color)


        if high_quality_verifying_graphics:
            write_text(screen, width // 2,  mode_y_level + mode_location_offset['Giant'] + big_text*3, 'Graphics: Fancy', small_text, background_color[0],
                       highlight_text_color)
        else:
            write_text(screen, width // 2,  mode_y_level + mode_location_offset['Giant'] + big_text*3, 'Graphics: Fast', small_text, background_color[0],
                       highlight_text_color)



        for index in range(min_index,max_index+1):
            music = music_list[index]
            location = index - music_pointer
            music_string = '%s' % (music)
            if location==0:
                music_string = '< %s >' % (music)
            write_text(screen, song_list_x_level, song_info_y_level + location*small_text, music_string , song_size_gradient[abs(location)],
                       background_color[0],
                       song_color_gradient[abs(location)])

        write_text(screen, song_list_x_level, song_info_y_level + 6*small_text , 'scroll', tiny_text, background_color[0],
                   highlight_text_color)
        draw_arrow('1up', screen, song_list_x_level, (song_info_y_level - 4*small_text))
        draw_arrow('1down', screen, song_list_x_level, (song_info_y_level + 4 * small_text))
        #print(song_info_list)
        write_text(screen, song_info_x_level, song_info_y_level - 1*small_text , 'BPM: %d'%song_info_list[0], tiny_text, background_color[0],
                   highlight_text_color)
        write_text(screen, song_info_x_level, song_info_y_level - 2*small_text , 'Length: %d sec.'%(song_info_list[1]//1000), tiny_text, background_color[0],
                   highlight_text_color)
        write_text(screen, song_info_x_level, song_info_y_level - 0*small_text , 'Difficulty: %d'%song_info_list[2], tiny_text, background_color[0],
                   highlight_text_color)
        write_text(screen, song_info_x_level, song_info_y_level + 1*small_text , 'Total points: %d'%song_info_list[3], tiny_text, background_color[0],
                   highlight_text_color)

        write_text(screen, width // 2, height-small_text, 'How to play: press %s,%s,%s,%s in appropriate timing!'%(guide_keys[0],guide_keys[1],guide_keys[2],guide_keys[3]), small_text, background_color[0],
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
        clock.tick(fps)

