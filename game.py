'''
Game loop

Nodes, holds, arcs

Distributer

Verifier
'''
import pygame
from variables import *
from tiles import *
from verifier_class import *
from distributer_class import *
from music_ import *
from text_writer import *
from image_processor import *
from score_viewer import *
from chart import *
from utility_functions import *

# exit할 때 해야 할 행동들을 모아놓은 함수
def exit_game(screen, clock, song_name, score,song_difficulty,total_points):
    view_score_menu(screen, clock, song_name, score,song_difficulty,total_points)

def get_ready(screen,clock,song_name,total_points):
    global change_background_color
    game_run = True
    exit_outer_game = False
    score = [0]
    pygame.mixer.music.stop()

    seconds_to_count = 3
    count = seconds_to_count
    start_time = pygame.time.get_ticks()

    while game_run:
        time_passed_milli = pygame.time.get_ticks() - start_time
        count = seconds_to_count - time_passed_milli//1000
        if count <= 0:
            game_run = False
            exit_outer_game = False
            break

        screen.fill(background_color[change_background_color])

        # Event handling
        keys = pygame.key.get_pressed()  # 꾹 누르고 있으면 계속 실행되는 것들
        if keys[pygame.K_f]:
            highlight_line(screen, 1)
        if keys[pygame.K_g]:
            highlight_line(screen, 2)
        if keys[pygame.K_h]:
            highlight_line(screen, 3)
        if keys[pygame.K_j]:
            highlight_line(screen, 4)
            #print(judgement_line)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:  # 윈도우를 닫으면 종료
                game_run = False
                exit_outer_game = True
                break

            if event.type == pygame.MOUSEMOTION:  # player가 마우스를 따라가도록
                # point.pos = pygame.mouse.get_pos()
                pass

            if event.type == pygame.MOUSEBUTTONUP:
                (xp, yp) = pygame.mouse.get_pos()
                pass

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # esc 키를 누르면 종료
                    game_run = False
                    exit_outer_game = True
                    break

                if event.key == pygame.K_f:
                    highlight_line(screen, 1)
                if event.key == pygame.K_g:
                    highlight_line(screen, 2)
                if event.key == pygame.K_h:
                    highlight_line(screen, 3)
                if event.key == pygame.K_j:
                    highlight_line(screen, 4)


        write_text(screen, width//2, (info_length//2)//2, 'Song: %s'%(song_name), small_text, background_color[change_background_color], highlight_text_color)
        write_text(screen, width // 2, (info_length // 2) // 2 + (info_length // 2), 'Score: %.2f' % score[0], small_text, background_color[change_background_color],
                   highlight_text_color)
        # draw basic frame with lines
        draw_frame(screen)

        write_text(screen, width // 2, height//2, '%d' % (count), giant_text,
                   background_color[change_background_color],
                   red_highlight_text_color)

        write_text(screen, width // 2, 3*(height//4), 'Press ECS to return to the main menu', tiny_text,
                   background_color[change_background_color],
                   red_highlight_text_color)

        # guide key shown
        draw_guide_key(screen)

        pygame.display.flip()
        clock.tick(fps)

    return exit_outer_game


def calc_song_progress_percent(song_length,song_start_time,current_time):  # return in percent
    if song_start_time == -1: # If song hasn't started
        return 0 # no progress!
    delta = current_time - song_start_time
    progress = 100*(delta/song_length)
    return progress


def run_FGHJ(screen,clock,song_name,stage_speed,offset,judgement_shown,guide_line_shown,high_quality_verifying_graphics):
    global bar_color, wait_delay, change_background_color
    game_run = True
    score = [0]
    chart_info = get_chart(song_name)
    total_points = chart_info[0]
    song_difficulty = chart_info[1]
    song_length = chart_info[2]  # in milliseconds!
    song_bpm = chart_info[3]

    # screen pause effect
    screen_freeze = False
    first_pause_time = song_length + 100 # no pause == pause after the end of the song


    nodes_on_screen = []
    holds_on_screen = []
    beat_lines = []
    tiles_off_screen = []

    if get_ready(screen,clock,song_name,total_points): # if exit outer game is true
        game_run = False
        view_score_menu(screen, clock, song_name, score, song_difficulty, total_points)
        return
    verifier = Verifier(screen,score,stage_speed,judgement_shown,song_bpm,high_quality_verifying_graphics)



    bar_pos = (width // 2, info_length//4)
    song_progress = 0

    song_start_time = -1
    need_music = True

    #print(chart_info[4])
    if chart_info[4]==[]:
        print("Chart has no nodes. Finishing the game.")
        exit_game(screen, clock, song_name, score, song_difficulty, total_points)
        game_run = False
    else:
        distributer = Distributer(stage_speed,offset,screen,chart_info[4],song_name,song_bpm,beat_line_request=guide_line_shown)


    while game_run:
        if need_music and distributer.ready:
            music_Q(song_name)
            need_music = False
            song_start_time = pygame.time.get_ticks()

        screen.fill(background_color[change_background_color])

        # Event handling
        keys = pygame.key.get_pressed()  # 꾹 누르고 있으면 계속 실행되는 것들
        if keys[pygame.K_f]:
            highlight_line(screen, 1)
        if keys[pygame.K_g]:
            highlight_line(screen, 2)
        if keys[pygame.K_h]:
            highlight_line(screen, 3)
        if keys[pygame.K_j]:
            highlight_line(screen, 4)
            #print(judgement_line)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:  # 윈도우를 닫으면 종료
                exit_game(screen, clock, song_name, score,song_difficulty,total_points)
                game_run = False
                break

            if event.type == pygame.MOUSEMOTION:  # player가 마우스를 따라가도록
                # point.pos = pygame.mouse.get_pos()
                pass

            if event.type == pygame.MOUSEBUTTONUP:
                (xp, yp) = pygame.mouse.get_pos()
                pass

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # esc 키를 누르면 종료
                    exit_game(screen, clock, song_name, score,song_difficulty,total_points)
                    game_run = False
                    break

                if event.key == pygame.K_f:
                    highlight_line(screen, 1)
                if event.key == pygame.K_g:
                    highlight_line(screen, 2)
                if event.key == pygame.K_h:
                    highlight_line(screen, 3)
                if event.key == pygame.K_j:
                    highlight_line(screen, 4)

        if not game_run:
            break

        distributer.distribute(nodes_on_screen,holds_on_screen,beat_lines)
        


        # 1. tile을 그린다
        for tile in nodes_on_screen+holds_on_screen:
            tile.move(stage_speed)
            tile.draw(screen)

        # 1-1. off screen tile을 움직인다
        for tile in tiles_off_screen:
            tile.move(stage_speed)


        # 2. guide line을 그린다
        if guide_line_shown:
            verifier.draw_guide_lines(nodes_on_screen,holds_on_screen,screen)

            for hori in beat_lines:
                hori.move(stage_speed)
                hori.draw(screen)


        # 3. 판정을 표시한다
        # verifier.node_check(nodes_on_screen, events)
        verifier.node_check(nodes_on_screen, tiles_off_screen, keys)
        verifier.hold_check(holds_on_screen, tiles_off_screen, keys)
        verifier.draw_judgement()

        # 3.1 special check after verifying (wait/change color etc.)
        #print(len(tiles_off_screen),end='')
        for tile in tiles_off_screen:
            #Note 의 special effect가 있을 경우 적용
            if tile.special:
                if (tile.y >= judgement_line): # after passing judgement line
                    #print('special found after judgement line')
                    special_effect = tile.special_effect()

                    # 3.2 do the special effect
                    if special_effect == 'wait':
                        first_pause_time = pygame.time.get_ticks()
                        screen_freeze = True

                        ####### change background color! ########
                        change_background_color = 1
                        screen.fill(background_color[change_background_color])
                        tile.fix_loc()
                        verifier.draw_judgement()
                        for T in tiles_off_screen + nodes_on_screen + holds_on_screen:
                            T.draw(screen,screen_freeze)
                        draw_frame(screen)
                        pygame.display.flip()
                        ####### change background color! ########
                        #pygame.time.delay(wait_delay)

                        tiles_off_screen.remove(tile)
                        break



        # 4. song progress를 표시한다(진행상황)
        current_time = pygame.time.get_ticks()  # in milliseconds
        song_progress = calc_song_progress_percent(song_length, song_start_time, current_time)
        draw_progress_bar(screen, song_progress, bar_pos[0], bar_pos[1])

        write_text(screen, width//2, (info_length//2)//2, 'Song: %s'%(song_name), small_text, bar_color, highlight_text_color)
        write_text(screen, width // 2, (info_length // 2) // 2 + (info_length // 2), 'Score: %.2f' % score[0], small_text, background_color[change_background_color],
                   highlight_text_color)

        # 5. 게임 틀을 그린다
        # draw basic frame with lines
        draw_frame(screen)

        if not screen_freeze:
            pygame.display.flip()
        else: # check when the screen update should be true
            screen_cur_time = pygame.time.get_ticks()
            if (screen_cur_time - first_pause_time) >= wait_delay:
                screen_freeze = False
                change_background_color = 0  # set back to normal

        clock.tick_busy_loop(fps)
        #clock.tick(fps)

        if check_music_ended(song_start_time):
            game_run = False
            exit_game(screen, clock, song_name, score,song_difficulty,total_points)
            break


def draw_progress_bar(screen, song_progress, x,y):
    global bar_color
    bar_width = width
    bar_height = info_length//2

    #draw_bar_frame(screen, x, y, bar_width, bar_height, color) # don't need frames here
    draw_bar(screen,x,y,bar_width,bar_height, song_progress, bar_color)


def draw_frame(screen):
    global frame_alpha,frame_alpha_max,frame_phase,frame_grad_color,change_background_color
    frame_line_width = 4
    frame_line_half = frame_line_width//2

    judgement_line_width = 4
    # pygame.draw.line(screen, judgement_line_color, [0, judgement_line-judgement_line_width//2], [width, judgement_line-judgement_line_width//2], judgement_line_width)
    pygame.draw.line(screen, judgement_line_color, [0, judgement_line],
                     [width, judgement_line], judgement_line_width)

    # fill in unsused lines
    pygame.draw.rect(screen, background_color[change_background_color],
                     [0-frame_line_half, info_length+frame_line_half, line_width, height-info_length])
    pygame.draw.rect(screen, background_color[change_background_color],
                     [width-line_width, info_length+frame_line_half, line_width, height-info_length])

    fill_color = (frame_grad_color,frame_grad_color,frame_grad_color)

    if frame_alpha == frame_alpha_max:
        frame_phase = -1/frame_cycle
    elif frame_alpha == 0:
        frame_phase = 1/frame_cycle
    frame_alpha = (frame_alpha + frame_phase)
    if (frame_alpha-int(frame_alpha)) < 1/(2*frame_cycle) :  # 이 주기일때만 업데이트
        frame_grad_color = min(40+int(frame_alpha),255)

    pygame.draw.rect(screen, fill_color,
                     [0-frame_line_half, info_length+frame_line_half, line_width, height-info_length])
    pygame.draw.rect(screen, fill_color,
                     [width-line_width, info_length+frame_line_half, line_width, height-info_length])

    pygame.draw.line(screen, line_color, [0,info_length//2], [width,info_length//2], frame_line_width)
    pygame.draw.line(screen, line_color, [0, info_length], [width, info_length], frame_line_width)

    for i in range((line_number-1)):
        pygame.draw.line(screen, line_color, [line_width*(i+1)-frame_line_half, info_length], [line_width*(i+1)-frame_line_half, height], frame_line_width)


def draw_guide_key(screen):
    global frame_grad_color,change_background_color
    for i in range((guide_key_size)):
        write_text(screen,guide_x_loc+line_width*i, guide_y_loc , guide_keys[i], small_text, background_color[change_background_color],
                   (color_safe(200-frame_grad_color),color_safe(200-frame_grad_color),color_safe(200-frame_grad_color)))


