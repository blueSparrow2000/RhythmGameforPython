'''
Verifier

노드를 판정함!

'''

import pygame
from variables import *
from text_writer import *
import math
from utility_functions import *

class Verifier():
    def __init__(self,screen, score,speed,judgement_shown,bpm,high_quality_verifying_graphics, given_fps):
        self.screen = screen
        self.speed = speed
        self.score = score
        self.tiles_to_verify = []
        self.judgement_frames = given_fps//2 #given_fps//2
        self.judgement_highest_pos = int((self.judgement_frames) *0.7)
        self.judgement_shown = judgement_shown
        self.high_quality_verifying_graphics = high_quality_verifying_graphics
        self.verification_show_time = 100 # ms

        self.frame_error = int(((10/given_fps)*self.speed) + 1)
        self.song_bpm = bpm
        song_mpb = ((1000 * 60 / self.song_bpm))
        self.half_bit_pixel_size = millisecond_pixel_converter(song_mpb, self.speed)/2
        self.appropriate_bit_pixel_size = self.half_bit_pixel_size/2
        # tolerances for node
        self.pure_perfect_tolerance =self.appropriate_bit_pixel_size * 0.2  # 20%
        self.perfect_tolerance = self.appropriate_bit_pixel_size* 0.4  # 40%
        self.hit_tolerance = self.appropriate_bit_pixel_size * 0.8  # 80 %
        self.judgement_tolerance = self.appropriate_bit_pixel_size  # Lost 판정범위

        # node guidelines
        self.color_gradient = [(200, 40, 40), (190, 150, 20), (90, 190, 130), (255, 255, 255), (180, 180, 180),
                               (180, 180, 180), (180, 180, 180)]

        # # tolerances for node
        # node_judgement_interval = int(self.speed**(1.3)/50) +self.frame_error
        # self.pure_perfect_tolerance = node_height // 10 + node_judgement_interval #10  #node_height // 2 + (1000 / given_fps) * (self.speed / 100)  # player의 반응속도를 고려한 판정 범위 pixel
        # self.perfect_tolerance = node_height // 4 + node_judgement_interval*1.2
        # self.hit_tolerance = node_height // 2 + node_judgement_interval*1.8 #50  #((node_height // 2)*(1 + self.speed/10))
        # self.judgement_tolerance = self.hit_tolerance + self.frame_error #self.hit_tolerance*(1+(10 / given_fps)*10)  #100  #((node_height // 2) * (1 + self.speed / 10))*1.3 # hit의 1.3배 범위
        #
        #
        #
        # if 1: #self.judgement_tolerance >= self.half_bit_pixel_size:  # exceeds to next beat
        #     self.pure_perfect_tolerance = self.half_bit_pixel_size*0.2 #20%
        #     self.perfect_tolerance = self.half_bit_pixel_size*0.4      # 40%
        #     self.hit_tolerance = self.half_bit_pixel_size*0.8          # 80 %
        #     self.judgement_tolerance = self.half_bit_pixel_size        # Lost 판정범위
        #     # self.color_gradient[0] = (0,0,0)

        self.node_judgement_line_half_sizes = [self.pure_perfect_tolerance,self.perfect_tolerance,self.hit_tolerance,self.judgement_tolerance]

        # tolerances for hold
        self.hold_hit_tolerance = int(5 + self.speed**(1.5)/50) #node_height // 4 + self.speed**(1.2)//4 #node_height // 4 + self.speed//4
        self.hold_ready_to_judge_range = self.hold_hit_tolerance*2
        self.hold_judgement_gap = self.hold_ready_to_judge_range *4

        self.error_tolerance = 0 # max(1,self.speed/20) # error due to frame or calculation time delay (speed 클수록 에러는 커짐)

        # hold guidelines
        self.hold_this_line_color = (255,255,255)


    def draw_guide_lines(self,nodes_on_screen,holds_on_screen,screen):
        self.draw_guide_lines_node(nodes_on_screen,screen)
        self.draw_guide_lines_hold(holds_on_screen,screen)


    ########## node
    def node_check(self,nodes_on_screen,tiles_off_screen,events):
        for node in nodes_on_screen:
            if node.check_border() or self.check_pressed(node,events):
                if node.special == 'BadApple':
                    tiles_off_screen.append(node)
                    nodes_on_screen.remove(node)
                    if self.check_pressed(node,events):
                        self.verify_judgement_node(node)
                    else: # lost
                        self.verify_judgement_node(node,enforce_Lost=True)
                    continue
                nodes_on_screen.remove(node)
                self.verify_judgement_node(node)







    def draw_guide_lines_node(self,nodes_on_screen,screen):
        for node in nodes_on_screen:
            for i in range(len(self.node_judgement_line_half_sizes)):
                judgement_half_size = self.node_judgement_line_half_sizes[i]
                pygame.draw.rect(screen, self.color_gradient[i],
                                 [line_axes[node.line - 1] - line_width // 2, node.y - judgement_half_size, line_width,
                                  2*judgement_half_size],1)


    def append_verification_tile(self,tile_verification):
        if self.high_quality_verifying_graphics:
            self.tiles_to_verify.append(tile_verification)
        else:
            tile_verification.append(pygame.time.get_ticks())
            #print(tile_verification)
            self.tiles_to_verify.append(tile_verification)


    def verify_judgement_node(self,node,enforce_Lost = False):

        point = 0
        result = ''
        detail = ''
        human_error = node.y - judgement_line

        if creater_mode:
            point=1
            result = "Tap"
            self.append_verification_tile([node, (result, detail), self.judgement_frames])
            self.score[0] += point
            return

        if enforce_Lost:
            self.append_verification_tile([node, ("Lost", ''), self.judgement_frames])
            if self.judgement_shown:
                print("Enforced Lost")
            return

        if self.judgement_shown:
            detail = 'Early' if ((human_error) <= 0) else 'Late'

        if abs(human_error) <= self.perfect_tolerance:
            result = "Perfect"

            if abs(human_error) <= self.pure_perfect_tolerance:
                detail = ''  # no detail for pure perfect!
                point = node.point
            else:
                point = node.point*0.95
        elif abs(human_error) <= self.hit_tolerance:

            result = "Hit"
            point = node.point*0.8
        else:
            result = "Lost"
            point = 0


        # print result of Lost/Hit/Perfect on the screen
        #print(result)
        self.append_verification_tile([node,(result,detail),self.judgement_frames])


        self.score[0] += point
        if self.judgement_shown:
            print(round(human_error))

    def check_pressed(self,node,events):  # 노드 동시에 눌러도 다 알 수 있게 함 (event만 쓰면 한번에 하나의 event만이 전달됨! 동시 클릭 불가)
        if (events[pygame.K_f] and node.line == 1) or (events[pygame.K_g] and node.line == 2) or (
                events[pygame.K_h] and node.line == 3) or (events[pygame.K_j] and node.line == 4):
                if abs(node.y - judgement_line) <= self.judgement_tolerance:
                        return True

    ############# hold
    def hold_check(self,holds_on_screen,tiles_off_screen,events):
        for hold in holds_on_screen:
            if self.hold_finished(hold) or hold.check_border(): # check border
                holds_on_screen.remove(hold)
                continue

            if self.hold_in_judgement_range(hold):  # 판정이 필요한 (널널하게 잡음. 컴퓨터 가비지 콜렉션 등 딜레이로 연산 패스할지도 모르니까)
                self.verify_judgement_hold(hold, events)


    def draw_guide_lines_hold(self,holds_on_screen,screen):
        guide_line_width = 4
        for hold in holds_on_screen:
            pygame.draw.line(screen, self.hold_this_line_color, [line_axes[hold.line - 1]-line_width//2, hold.this_judgement_pos], [line_axes[hold.line]-line_width//2, hold.this_judgement_pos], guide_line_width)


    def verify_judgement_hold(self,hold, events):
        point = 0
        result = ''
        detail = ''

        if creater_mode:
            result = "Hold"
            # hold 점수를 계산 (hold의 총 점수를 check point 개수로 나눔)
            hold_point = round(
                hold.point / (math.ceil((hold.length/ self.hold_judgement_gap))),5)
            #print(hold_point)
            point = hold_point
        else:
            if not self.hold_ready_to_hit(hold):  # holding판정 범위 밖일때
                if self.passed_last_chance(hold):
                    result = "Lost"
                    point = 0
                else: # do nothing
                    return
            else: # holding판정 범위안에 들어왔을 때
                if self.check_keep_pressing(hold,events): # 한번이라도 누르고 있었다면
                    result = "Holding"
                    # hold 점수를 계산 (hold의 총 점수를 check point 개수로 나눔)
                    hold_point = round(
                        hold.point / (math.ceil((hold.length/ self.hold_judgement_gap))),5)
                    #print(hold_point)
                    point = hold_point
                else: # 아직은 누르지 않은 상태 ==> do nothing (이러다가 패스해버리면 위의 if에 걸림)
                    return

        #print(result)
        #print("sending %s to"%hold.this_judgement_pos)
        self.append_verification_tile([hold,(result,detail),self.judgement_frames])
        self.score[0] += point
        self.update_hold_judgement_pos(hold)
        if result=="Lost":
            hold.holding = False
            hold.update_color()
        else:
            hold.holding = True
            hold.update_color()
        #print("here: ",hold.this_judgement_pos)
        # print result of Lost/Hit/Perfect on the screen
        # print(result)

    def hold_in_judgement_range(self,hold): # 판정이 필요한 범위(널널하게 gap의 절반으로 잡음)에 들어왔을 때만 계산하도록 (너무 멀리 있는 노드 제외하기!)
        # hold.this_judgement_pos가 판정선과 가까운 경우
        return abs(hold.this_judgement_pos-judgement_line) <= (self.hold_ready_to_judge_range + self.error_tolerance)

    def hold_ready_to_hit(self,hold):
        if abs(judgement_line - hold.this_judgement_pos) <= (self.hold_hit_tolerance):
            return True

    def passed_last_chance(self,hold):
        if (hold.this_judgement_pos - judgement_line) > (self.hold_hit_tolerance):
            return True


    def ending_phase(self,hold):
        return (hold.this_judgement_pos - hold.tail) <= self.hold_judgement_gap

    def hold_finished(self,hold):
        return (hold.this_judgement_pos >= (height + self.hold_judgement_gap - self.frame_error)) and (hold.tail - judgement_line) > (self.hold_hit_tolerance)

    def update_hold_judgement_pos(self,hold):
        global height
        if self.ending_phase(hold): # ending phase인 경우, 마디를 height + self.hold_judgement_gap로 보내버림 (다시는 판정범위 들어오지 않게!)
            hold.this_judgement_pos = height + self.hold_judgement_gap
            #print("Ending!")
        else:
            hold.this_judgement_pos -= self.hold_judgement_gap

    def check_keep_pressing(self,hold,keys):
        if (keys[pygame.K_f] and hold.line == 1) or (keys[pygame.K_g] and hold.line == 2) or (keys[pygame.K_h] and hold.line == 3) or (keys[pygame.K_j] and hold.line == 4):
            return True


    def draw_judgement(self):
        if self.high_quality_verifying_graphics:
            for i in range(len(self.tiles_to_verify)-1,-1,-1):
                verification = self.tiles_to_verify[i]
                if verification[2] <= 1:
                    self.tiles_to_verify.remove(verification)
                else:
                    write_text(self.screen, line_axes[verification[0].line-1], judgement_line -judgement_text*3 + self.calc_pos(verification[2]), "%s"%(verification[1][0]), judgement_text, background_color[0], highlight_text_color)
                    write_text(self.screen, line_axes[verification[0].line - 1],
                               judgement_line - judgement_text * 3 + self.calc_pos(verification[2])+judgement_text,
                               "%s" % (verification[1][1]), detail_text, background_color[0], highlight_text_color)
                    verification[2] -= 1
        else:
            cur_time = pygame.time.get_ticks()
            for i in range(len(self.tiles_to_verify) - 1, -1, -1):
                verification = self.tiles_to_verify[i]
                if cur_time - verification[3] > self.verification_show_time:
                    self.tiles_to_verify.remove(verification)
                else:
                    write_text(self.screen, line_axes[verification[0].line - 1],
                               judgement_line - judgement_text * 3,
                               "%s" % (verification[1][0]), judgement_text, background_color[0], highlight_text_color)
                    write_text(self.screen, line_axes[verification[0].line - 1],
                               judgement_line - judgement_text * 3 + judgement_text,
                               "%s" % (verification[1][1]), detail_text, background_color[0], highlight_text_color)



    def calc_pos(self,note_stage):
        return (max(self.judgement_highest_pos, note_stage) - self.judgement_highest_pos)









