import pygame
from variables import *
from music_ import *
from text_writer import *
from image_processor import *

def view_score_menu(screen,clock,song_name,score_pointer,song_difficulty,total_points):
    score = score_pointer[0]
    music_Q('Another way',True)
    viewer_run = True

    score_percentage = 0
    if total_points!=0:
        score_percentage = round((score / total_points) * 100, 3)
    score_percentage_loc = height//3 + title_text*2

    grade = score_grader(score_percentage)
    grade_sticker_loc = height//3 + title_text*4 + sticker_text//2

    # score bar options
    alpha = 0
    alpha_max = 100
    score_color = score_colors[grade]
    bar_pos = (width // 2, height//3 + title_text*3)

    # acknowledge credit
    credits = get_music_info(song_name)
    credits_loc = grade_sticker_loc + sticker_text*4


    while viewer_run:
        screen.fill(background_color[0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 윈도우를 닫으면 종료
                viewer_run = False
                break

            if event.type == pygame.MOUSEMOTION:  # player가 마우스를 따라가도록
                # point.pos = pygame.mouse.get_pos()
                pass

            if event.type == pygame.MOUSEBUTTONUP:
                (xp, yp) = pygame.mouse.get_pos()
                pass

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:  # esc 키를 누르면 종료
                    viewer_run = False
                    break

        if not viewer_run:
            break

        write_text(screen, width // 2, height//20 , 'Press Enter to continue', small_text, background_color[0],
                   highlight_text_color)

        write_text(screen, width // 2, height//4, '%s' % (song_name), big_text, background_color[0],
                   highlight_text_color)
        write_text(screen, width // 2, height//4 + big_text*2, 'Song difficulty: %s' % (song_difficulty), small_text, background_color[0],
                   highlight_text_color)

        # write_text(screen, width // 2, height//3 + title_text*2, 'Score: %.2f' % score, small_text,
        #            background_color[0],
        #            highlight_text_color)

        write_text(screen, width // 2, score_percentage_loc, 'Score Percentage: %.3f%%' % (score_percentage), small_text,
                   background_color[0],
                   highlight_text_color)


        draw_score_bar(screen, score_percentage,score_color,alpha/alpha_max,bar_pos[0],bar_pos[1])
        if alpha < alpha_max:
            alpha += 1


        write_text(screen, width // 2, grade_sticker_loc , '%s' % (grade), sticker_text,
                   background_color[0],
                   score_color )


        write_text(screen, width//2, credits_loc, "< Copyright Acknowledgement(CC) >", small_text, background_color[0],
                   red_highlight_text_color)

        write_text(screen, width//2, credits_loc+big_text, "'%s' song credits (link in README.md also):"%song_name, tiny_text, background_color[0],
                   highlight_text_color)

        for i in range(len(credits)):
            write_text(screen, width//2, credits_loc +big_text*2+ small_text*(i+1),
                       '%s'%credits[i], tiny_text, background_color[0],
                       highlight_text_color)


        pygame.display.flip()
        clock.tick_busy_loop(fps)


def draw_score_bar(screen, score_percentage, color, alpha,x,y):
    bar_width = (width//3)*2
    bar_height = big_text

    draw_bar_frame(screen, x, y, bar_width, bar_height, color)
    draw_bar(screen,x,y,bar_width,bar_height, score_percentage*alpha, color)


def score_grader(score_percentage):
    if score_percentage== 100:
        return 'Pure Perfect!!! (PP)'
    if score_percentage== 98:
        return 'Perfect!! (P)'
    elif score_percentage> 95:
        return 'AA'
    elif score_percentage> 92:
        return 'A'
    elif score_percentage> 86:
        return 'B'
    elif score_percentage> 80:
        return 'C'
    elif score_percentage> 70:
        return 'D'
    elif score_percentage> 50:
        return 'E'
    else:
        return 'Failed'
