import pygame
from variables import *
from music_ import *
from text_writer import *
from image_processor import *
from utility_functions import *
from chart import *
from game import *
from chart_builder import update_chart


def exit_option_screen(stage_speed, offset, judgement_shown, guide_line_shown, high_quality_verifying_graphics):
    return stage_speed, offset, judgement_shown, guide_line_shown, high_quality_verifying_graphics


def option_screen(screen,clock,stage_speed, offset, judgement_shown, guide_line_shown, high_quality_verifying_graphics):
    # Variables needed to run run_FGHJ (the main function)
    # Used after song selection

    pygame.mixer.music.stop()
    #music_Q(scoreboardMusic,True)
    option_screen_run = True


    # option settings
    mode_y_level =  (height // 5 )* 2
    offset_x_level = (width//7)*2
    toggle_y_level = height // 2
    # {'[mode name]':([mode location offset on screen], [value of adjustment])}
    mode_location_offset = {'Giant':big_text*4,'huge':big_text*3+small_text,'big':big_text*2+small_text,'small':big_text}
    offset_mode = {'10up':(-mode_location_offset['big'],10), '1up':(-mode_location_offset['small'],1),'10down':(mode_location_offset['big'],-10), '1down':(mode_location_offset['small'],-1)}
    offset_mode_keys = offset_mode.keys()
    speed_x_level = (width//7)*5
    speed_mode = {'10up':(-mode_location_offset['big'],10), '1up':(-mode_location_offset['small'],1),'10down':(mode_location_offset['big'],-10), '1down':(mode_location_offset['small'],-1)}
    speed_mode_keys = speed_mode.keys()

    # back button
    back = load_image('back')
    back = resize_image(back, (big_text,big_text))
    back_rect = move_image(back, (back_button_x_loc,back_button_y_loc))



    while option_screen_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 윈도우를 닫으면 종료
                option_screen_run = False
                return exit_option_screen(stage_speed, offset, judgement_shown, guide_line_shown, high_quality_verifying_graphics)

            if event.type == pygame.MOUSEMOTION:  # player가 마우스를 따라가도록
                # point.pos = pygame.mouse.get_pos()
                pass

            if event.type == pygame.MOUSEBUTTONUP:
                (xp, yp) = pygame.mouse.get_pos()
                mouse_particle_list.append((pygame.time.get_ticks(), (xp, yp)))
                mouse_click_sound()

                if abs(xp - back_button_x_loc - big_text) < big_text:  # press back button to quit song selection
                    if abs(yp - back_button_y_loc) < big_text:
                        option_screen_run = False
                        return exit_option_screen(stage_speed, offset, judgement_shown, guide_line_shown, high_quality_verifying_graphics)


                if abs(xp - offset_x_level) < big_text * 2:
                    for offset_ in offset_mode_keys:
                        if abs(yp - (mode_y_level + offset_mode[offset_][0])) < big_text // 2:
                            offset += offset_mode[offset_][1] * 10
                            offset = boundary_checker(min_offset, max_offset, offset)

                if abs(xp - speed_x_level) < big_text * 2:
                    for speed_ in speed_mode_keys:
                        if abs(yp - (mode_y_level + speed_mode[speed_][0])) < big_text // 2:
                            stage_speed += speed_mode[speed_][1]
                            stage_speed = boundary_checker(min_speed, max_speed, stage_speed)


                if abs(xp - width // 2) < big_text * 3:  # update chart
                    if abs(yp - (toggle_y_level + mode_location_offset[
                        'huge'] - big_text + big_text // 2)) < big_text // 2:
                        update_chart()

                if abs(xp - width // 2) < big_text * 3:  # toggle judgement
                    if abs(yp - (toggle_y_level + mode_location_offset[
                        'huge'] + big_text + big_text // 2)) < big_text // 2:
                        judgement_shown = not judgement_shown  # not judgement_shown

                if abs(xp - width // 2) < big_text * 3:  # toggle guide line
                    if abs(yp - (toggle_y_level + mode_location_offset[
                        'huge'] + big_text * 3 + big_text // 2)) < big_text // 2:
                        guide_line_shown = not guide_line_shown

                if abs(xp - width // 2) < big_text * 3:  # toggle graphics
                    if abs(yp - (toggle_y_level + mode_location_offset[
                        'huge'] + big_text * 5 + big_text // 2)) < big_text // 2:
                        high_quality_verifying_graphics = not high_quality_verifying_graphics

                if abs(xp - width // 2) < big_text * 3:  # toggle sound effect
                    if abs(yp - (toggle_y_level + mode_location_offset[
                        'huge'] + big_text * 7 + big_text // 2)) < big_text // 2:
                        sound_effect[0] = not sound_effect[0]

                if abs(xp - width // 2) < big_text * 3:  # toggle particle effect
                    if abs(yp - (toggle_y_level + mode_location_offset[
                        'huge'] + big_text * 8 + big_text // 2)) < big_text // 2:
                        particle_effect[0] = not particle_effect[0]



            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    option_screen_run = False
                    return exit_option_screen(stage_speed, offset, judgement_shown, guide_line_shown, high_quality_verifying_graphics)

        if not option_screen_run:
            return exit_option_screen(stage_speed, offset, judgement_shown, guide_line_shown, high_quality_verifying_graphics)

        screen.fill(background_color[0])

        # draw keys
        if creater_mode:
            write_text(screen, width // 2, small_text * 2, '- This is a creater mode -', small_text,
                       background_color[0],
                       debug_color)

        write_text(screen, width // 2, height // 8 - big_text, 'Options', big_text, background_color[0],
                   highlight_text_color)
        pygame.draw.rect(screen, highlight_text_color, [width//4 - big_text, height // 8 - big_text - button_y_offset, button_x_size, button_y_size], 4,8)



        # option settings
        for offset_ in offset_mode_keys:
            draw_arrow(offset_, screen, offset_x_level, (mode_y_level + offset_mode[offset_][0]))

        write_text(screen, offset_x_level, mode_y_level - mode_location_offset['huge'], 'Late (+)', tiny_text,
                   background_color[0],
                   highlight_text_color)
        write_text(screen, offset_x_level, mode_y_level + mode_location_offset['huge'], 'Early (-)', tiny_text,
                   background_color[0],
                   highlight_text_color)

        if offset <0:
            write_text(screen, offset_x_level, mode_y_level + mode_location_offset['huge'] + 50, '[WARNING]', small_text,
                       background_color[0],
                       red_highlight_text_color)
            write_text(screen, offset_x_level, mode_y_level + mode_location_offset['huge'] + 50 + small_text, 'Negative offset (with low speed)', tiny_text,
                       background_color[0],
                       red_highlight_text_color)
            write_text(screen, offset_x_level, mode_y_level + mode_location_offset['huge'] + 50 + small_text*2, 'may crash the game!', tiny_text,
                       background_color[0],
                       red_highlight_text_color)

        for speed_ in speed_mode_keys:
            draw_arrow(speed_, screen, speed_x_level, (mode_y_level + speed_mode[speed_][0]))


        write_text(screen, offset_x_level, mode_y_level, 'Offset: %d (ms)' % (offset), small_text,
                   background_color[0],
                   highlight_text_color)
        write_text(screen, speed_x_level, mode_y_level, 'Speed: %d' % (stage_speed), small_text,
                   background_color[0],
                   highlight_text_color)


        write_text(screen, width // 2, toggle_y_level + mode_location_offset['Giant'] - big_text,
                   '<Update chart>', small_text, background_color[0],
                   highlight_text_color)


        if judgement_shown:
            write_text(screen, width // 2, toggle_y_level + mode_location_offset['Giant'] + big_text,
                       'Judgement detail: On', small_text, background_color[0],
                       highlight_text_color)
        else:
            write_text(screen, width // 2, toggle_y_level + mode_location_offset['Giant'] + big_text,
                       'Judgement detail: Off', small_text, background_color[0],
                       highlight_text_color)

        if guide_line_shown:
            write_text(screen, width // 2, toggle_y_level + mode_location_offset['Giant'] + big_text * 3,
                       'Guide line: On', small_text, background_color[0],
                       highlight_text_color)
        else:
            write_text(screen, width // 2, toggle_y_level + mode_location_offset['Giant'] + big_text * 3,
                       'Guide line: Off', small_text, background_color[0],
                       highlight_text_color)

        if high_quality_verifying_graphics:
            write_text(screen, width // 2, toggle_y_level + mode_location_offset['Giant'] + big_text * 5,
                       'Graphics: Fancy', small_text, background_color[0],
                       highlight_text_color)
        else:
            write_text(screen, width // 2, toggle_y_level + mode_location_offset['Giant'] + big_text * 5,
                       'Graphics: Fast', small_text, background_color[0],
                       highlight_text_color)


        if sound_effect[0]:
            write_text(screen, width // 2, toggle_y_level + mode_location_offset['Giant'] + big_text * 7,
                       'Sound effects: On', small_text, background_color[0],
                       highlight_text_color)
        else:
            write_text(screen, width // 2, toggle_y_level + mode_location_offset['Giant'] + big_text * 7,
                       'Sound effects: Off', small_text, background_color[0],
                       highlight_text_color)

        if particle_effect[0]:
            write_text(screen, width // 2, toggle_y_level + mode_location_offset['Giant'] + big_text * 8,
                       'Particle effects: On', small_text, background_color[0],
                       highlight_text_color)
        else:
            write_text(screen, width // 2, toggle_y_level + mode_location_offset['Giant'] + big_text * 8,
                       'Particle effects: Off', small_text, background_color[0],
                       highlight_text_color)


        # draw the back button
        screen.blit(back, back_rect)


        if mouse_particle_list:  # if not empty
            # print(len(mouse_particle_list))
            current_run_time = pygame.time.get_ticks()
            for mouse_particle in mouse_particle_list:
                # draw_particle(screen, mouse_particle)
                mouse_click_time = mouse_particle[0]
                position = mouse_particle[1]
                delta = (current_run_time - (mouse_click_time)) / 1000
                if delta >= water_draw_time_mouse:
                    mouse_particle_list.remove(mouse_particle)
                factor = delta / water_draw_time_mouse
                radi = calc_drop_radius(factor, mouse_particle_radius)
                pygame.draw.circle(screen, effect_color, position, radi, particle_width_mouse)

        pygame.display.flip()
        clock.tick(main_loop_render_fps)
