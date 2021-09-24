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

# exit할 때 해야 할 행동들을 모아놓은 함수
def exit_game(screen, clock, song_name, score,song_difficulty,total_points):
    view_score_menu(screen, clock, song_name, score,song_difficulty,total_points)

def get_ready(screen,clock,song_name,total_points):
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

        screen.fill(background_color[0])

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


        write_text(screen, width//2, (info_length//2)//2, 'Song: %s'%(song_name), small_text, background_color[0], highlight_text_color)
        write_text(screen, width // 2, (info_length // 2) // 2 + (info_length // 2), 'Score: %.2f' % score[0], small_text, background_color[0],
                   highlight_text_color)
        # draw basic frame with lines
        draw_frame(screen)

        write_text(screen, width // 2, height//2, '%d' % (count), giant_text,
                   background_color[0],
                   red_highlight_text_color)

        pygame.display.flip()
        clock.tick(fps)

    return exit_outer_game


def calc_song_progress_percent(song_length,song_start_time,current_time):  # return in percent
    if song_start_time == -1: # If song hasn't started
        return 0 # no progress!
    delta = current_time - song_start_time
    progress = 100*(delta/song_length)
    return progress


def run_FGHJ(screen,clock,song_name,stage_speed,offset,judgement_shown,guide_line_shown):
    game_run = True
    score = [0]
    chart_info = get_chart(song_name)
    total_points = chart_info[0]
    song_difficulty = chart_info[1]
    song_length = chart_info[2]  # in milliseconds!
    song_bpm = chart_info[3]

    nodes_on_screen = []
    holds_on_screen = []
    beat_lines = []

    if get_ready(screen,clock,song_name,total_points): # if exit outer game is true
        game_run = False
        view_score_menu(screen, clock, song_name, score, song_difficulty, total_points)
        return
    verifier = Verifier(screen,score,stage_speed,judgement_shown,song_bpm)


    bar_color = (90,90,90)
    bar_pos = (width // 2, info_length//4)
    song_progress = 0

    song_start_time = -1
    need_music = True

    distributer = Distributer(stage_speed,offset,screen,chart_info[4],song_name,song_bpm,beat_line_request=guide_line_shown)

    while game_run:
        if need_music and distributer.ready:
            music_Q(song_name)
            need_music = False
            song_start_time = pygame.time.get_ticks()

        screen.fill(background_color[0])

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

        # 2. guide line을 그린다
        if guide_line_shown:
            verifier.draw_guide_lines(nodes_on_screen,holds_on_screen,screen)

            for hori in beat_lines:
                hori.move(stage_speed)
                hori.draw(screen)


        # 3. 판정을 표시한다
        # verifier.node_check(nodes_on_screen, events)
        verifier.node_check(nodes_on_screen,keys)
        verifier.hold_check(holds_on_screen, keys)
        verifier.draw_judgement()



        # 4. song progress를 표시한다(진행상황)
        current_time = pygame.time.get_ticks()  # in milliseconds
        song_progress = calc_song_progress_percent(song_length, song_start_time, current_time)
        draw_progress_bar(screen, song_progress, bar_color, bar_pos[0], bar_pos[1])

        write_text(screen, width//2, (info_length//2)//2, 'Song: %s'%(song_name), small_text, background_color[0], highlight_text_color)
        write_text(screen, width // 2, (info_length // 2) // 2 + (info_length // 2), 'Score: %.2f' % score[0], small_text, background_color[0],
                   highlight_text_color)

        # 5. 게임 틀을 그린다
        # draw basic frame with lines
        draw_frame(screen)


        pygame.display.flip()
        clock.tick_busy_loop(fps)
        #clock.tick(fps)

        if check_music_ended(song_start_time):
            game_run = False
            exit_game(screen, clock, song_name, score,song_difficulty,total_points)
            break


def draw_progress_bar(screen, song_progress, color,x,y):
    bar_width = width
    bar_height = info_length//2

    #draw_bar_frame(screen, x, y, bar_width, bar_height, color) # don't need frames here
    draw_bar(screen,x,y,bar_width,bar_height, song_progress, color)


def draw_frame(screen):
    global frame_alpha,frame_alpha_max,frame_phase,frame_grad_color
    frame_line_width = 4

    judgement_line_width = 4
    # pygame.draw.line(screen, judgement_line_color, [0, judgement_line-judgement_line_width//2], [width, judgement_line-judgement_line_width//2], judgement_line_width)
    pygame.draw.line(screen, judgement_line_color, [0, judgement_line],
                     [width, judgement_line], judgement_line_width)

    # fill in unsused lines
    pygame.draw.rect(screen, background_color[0],
                     [0-frame_line_width//2, info_length+frame_line_width//2, line_width, height-info_length])
    pygame.draw.rect(screen, background_color[0],
                     [width-line_width, info_length+frame_line_width//2, line_width, height-info_length])

    fill_color = (frame_grad_color,frame_grad_color,frame_grad_color)

    if frame_alpha == frame_alpha_max:
        frame_phase = -1/frame_cycle
    elif frame_alpha == 0:
        frame_phase = 1/frame_cycle
    frame_alpha = (frame_alpha + frame_phase)
    if (frame_alpha-int(frame_alpha)) < 1/(2*frame_cycle) :  # 이 주기일때만 업데이트
        frame_grad_color = min(40+int(frame_alpha),255)

    pygame.draw.rect(screen, fill_color,
                     [0-frame_line_width//2, info_length+frame_line_width//2, line_width, height-info_length])
    pygame.draw.rect(screen, fill_color,
                     [width-line_width, info_length+frame_line_width//2, line_width, height-info_length])

    pygame.draw.line(screen, line_color, [0,info_length//2], [width,info_length//2], frame_line_width)
    pygame.draw.line(screen, line_color, [0, info_length], [width, info_length], frame_line_width)

    for i in range((line_number-1)):
        pygame.draw.line(screen, line_color, [line_width*(i+1)-frame_line_width//2, info_length], [line_width*(i+1)-frame_line_width//2, height], frame_line_width)





