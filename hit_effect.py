import pygame
import random
from variables import *

class Particle():
    def __init__(self, start_loc,start_size):
        self.x, self.y = start_loc
        self.size = start_size
        self.remove_flag = False
        self.xdirection = (random.randint(0,1)*2 - 1) *random.randint(1,4)
        self.ydirection = random.randint(-2,2)

    def move(self):
        self.x += self.xdirection
        self.y += self.ydirection

    def draw(self,screen):
        pygame.draw.rect(screen, node_color[change_background_color[0]],
                         [ self.x, self.y, self.size,self.size], border_radius = 2)

    def update(self):
        self.size -= 1
        self.check()

    def check(self):
        if self.size <= 4:
            self.remove_flag = True



def hit_effect(screen,effect_queue):
    #print(effect_queue)
    for effect in effect_queue:
        # draw effects
        effect.move()
        effect.draw(screen)
        effect.update()

        if effect.remove_flag == True:
            effect_queue.remove(effect)

def append_effect(effect_queue, lane):
    for i in range(5):
        effect_queue.append( Particle((line_width * (lane) + line_width // 2, judgement_line - 10), 20) )

'''
################################### TEST PARTICLES
test_particles_on = False


def draw_frame(screen):
    global frame_alpha,frame_alpha_max,frame_phase,frame_grad_color,change_background_color
    frame_line_width = 4
    frame_line_half = frame_line_width//2

    judgement_line_width = 4
    # pygame.draw.line(screen, judgement_line_color, [0, judgement_line-judgement_line_width//2], [width, judgement_line-judgement_line_width//2], judgement_line_width)
    pygame.draw.line(screen, judgement_line_color, [0, judgement_line],
                     [width, judgement_line], judgement_line_width)

    # fill in unsused lines
    pygame.draw.rect(screen, background_color[change_background_color[0]],
                     [0-frame_line_half, info_length+frame_line_half, line_width, height-info_length])
    pygame.draw.rect(screen, background_color[change_background_color[0]],
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


if test_particles_on:
    one_particle = True
    effect_queue = []
    pygame.init()  # 파이게임 초기화
    clock = pygame.time.Clock()
    # computer screen size: 1920 x 1080

    screen = pygame.display.set_mode((width, height))  # window 생성
    pygame.display.set_caption('Paticle test')  # window title
    width, height = pygame.display.get_surface().get_size()  # window width, height

    screen.fill(background_color[0])  # background color

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 윈도우를 닫으면 종료
                run = False
                break
            if event.type == pygame.MOUSEMOTION:
                # player가 마우스를 따라가도록
                # point.pos = pygame.mouse.get_pos()
                pass

            if event.type == pygame.MOUSEBUTTONUP:
                (xp, yp) = pygame.mouse.get_pos()
                append_effect(effect_queue, 1)

        screen.fill(background_color[0])
        draw_frame(screen)



        if one_particle:
            one_particle = False
            lane = 1 # first lane
            append_effect(effect_queue, lane)


        hit_effect(screen,effect_queue)

        pygame.display.flip()
        clock.tick(main_loop_render_fps)
        
'''
