'''
Specific chart generator for each songs
This is going to be removed when 'Game maker' is developed!

0. Copy the template (entire chart_H2O.py file) and rename filename & class name properly.
1. Add self.song_name. This should be same with the sound file name in /CC_music/ folder!
2. define build_chart function and add patterns as you want!
It must include: (every thing should be safely converted to integer)
- song length [milliseconds]
- song_bpm (calculate it from the online sites!)
- song_difficulty (as you wish ^^)
- total_points or # of nodes (as you wish ^^)

'''
from variables import *
from chart_patterns import *

class Chart_BadApple():
    def __init__(self):
        self.song_name = 'BadApple'

    def build_chart(self,full_path):
        global wait_delay
        ##################################### fill in
        song_length = 46500
        song_bpm = 138
        cycle = 4
        song_mpb = ((1000 * 60 / song_bpm) / cycle)  # milli-seconds per beat
        song_difficulty = 3
        number_of_nodes = 92 # 95
        recommended_fps = 60

        song_offset = -230
        s1 = 438
        s2 = 109
        s3 = 200
        s4 = 4 * s1
        hold_len = s1 // 2 - 50
        ####################################

        with open("%s" % full_path, "w") as f:
            f.write('%d,%d,%d,%d,%d\n' % (song_length, song_bpm, song_difficulty, number_of_nodes,recommended_fps))
            ############## phase 1 ###########
            beat_pos = song_offset
            very_first_node = True

            for j in range(4):
                for i in range(3):
                    if very_first_node:
                        pattern = write_multi_tiles('N__H', beat_pos,['1/','','','1/300'])
                        beat_pos += s1
                        f.write(pattern)
                        very_first_node = False
                    else:
                        pattern = basic_strike(beat_pos, 1, 1)
                        beat_pos += s1
                        f.write(pattern)

                # using hold
                pattern = basic_hold(beat_pos+50, 3, 1, hold_len)
                beat_pos += s2 * 2
                f.write(pattern)
                pattern = basic_hold(beat_pos+50, 4, 1, hold_len)
                beat_pos += s2 * 2
                f.write(pattern)

                ##### using individual check
                # pattern = basic_strike(beat_pos, 3, 1)
                # f.write(pattern)
                # pattern = basic_strike(beat_pos+s2, 4, 1)
                # f.write(pattern)
                # pattern = basic_strike(beat_pos+s2*2, 3, 1)
                # f.write(pattern)
                # pattern = basic_strike(beat_pos+s2*3, 4, 1)
                # f.write(pattern)
                # beat_pos += s2*4

                # pattern = quadro_loscilate_(beat_pos+10, 4, 4, s2)
                # beat_pos += s2*4 +100
                # f.write(pattern)

                pattern = basic_strike(beat_pos+30, 1, 1)
                beat_pos += s1
                f.write(pattern)

                for i in range(2):
                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s1
                    f.write(pattern)

                if j==3:
                    pattern = basic_strike(beat_pos-30, 1, 1, 'BadApple') # special node!
                    beat_pos += s3 #- wait_delay # delay
                    f.write(pattern)
                    break
                pattern = basic_strike(beat_pos, 1, 1)
                beat_pos += s3
                f.write(pattern)
                pattern = basic_strike(beat_pos, 1, 1)
                beat_pos += s3
                f.write(pattern)


            ##################################


            beat_pos += s1//2 # phase transfer
            ############## phase 2A ###########
            for l in range(2):
                for j in range(4):
                    for i in range(3):
                        pattern =''
                        if i==1:
                            pattern = basic_hold(beat_pos+l*10, 2, 1, hold_len * 2)
                        else:
                            pattern = basic_hold(beat_pos+l*10, 1, 1, hold_len*2)
                        beat_pos += s1*2
                        f.write(pattern)

                    if j==3:
                        if l==0:
                            beat_pos -= 30  # error accumulation
                        for kk in range(2):
                            for k in range(3):
                                pattern=''
                                if kk==0:
                                    pattern = basic_strike(beat_pos, 2+k, 1)
                                else:
                                    pattern = basic_strike(beat_pos, 4-k, 1)
                                beat_pos += s1//3
                                f.write(pattern)
                        beat_pos -= 30
                        break

                    for i in range(2):
                        pattern = ''
                        if j%2==0:
                            pattern = basic_hold(beat_pos, 3+i, 1, hold_len)
                        else:
                            pattern = basic_hold(beat_pos, 4-i, 1, hold_len)
                        beat_pos += s1
                        f.write(pattern)
                    beat_pos -= 10 # error accumulation
                beat_pos -=30 # error accumulation


            ##################################



            ############## phase 3 ###########
            for l in range(2):
                pattern = basic_hold(beat_pos, 1, 1, hold_len * 2)
                beat_pos += s1*2
                f.write(pattern)

                pattern = basic_hold(beat_pos, 2, 1, hold_len)
                beat_pos += s1*2
                f.write(pattern)
            ##################################







