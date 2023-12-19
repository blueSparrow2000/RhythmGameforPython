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

class Chart_HHM():
    def __init__(self):
        self.song_name = 'HHM' #'HHM_climax'

    def build_chart(self,full_path):
        global wait_delay
        ##################################### fill in
        song_length = 104200
        song_bpm = 168 # 112*2
        song_mpb = ((1000 * 60 / song_bpm)) # 53.5 about 54 # milli-seconds per beat
        song_difficulty = 4
        number_of_nodes = 100# 95

        song_offset = 10600

        s1 = 426
        s2 = s1//2
        s3 = s2 + s1//4
        s4 = s1//4
        s8 = s1//8
        s16 = s1//16
        s32 = s1//32
        ming = s8*6

        #song_offset = -520  # for climax

        ####################################

        with open("%s" % full_path, "w") as f:
            f.write('%d,%d,%d,%d\n' % (song_length, song_bpm, song_difficulty, number_of_nodes))
            ############## phase 1 ###########
            beat_pos = song_offset

            #
            for j in range(2):
                for i in range(2):
                    ### 흠 흐밍
                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s1 - s16
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 3, 1)
                    beat_pos += s2 + s4 + s8
                    f.write(pattern)

                    ### 흠 흐 흠
                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s2 + s4
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2 - s16
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s1 - s8
                    f.write(pattern)

                    ### 흐
                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2 - s16
                    f.write(pattern)


                    if i==0:
                        beat_pos += s8
                        ### 밍밍밍
                        pattern = pattern = basic_hold(beat_pos, 3, 1, s1 + s16)
                        beat_pos += s1 + s2 + s4
                        f.write(pattern)

                    else:
                        ##########################
                        beat_pos += s4 + s16 + s32
                        ### 밍 흠
                        pattern = basic_strike(beat_pos, 3, 1)
                        beat_pos += s2 + s4 + s16
                        f.write(pattern)

                        pattern = basic_strike(beat_pos, 1, 1)
                        beat_pos += s1 - s8 - s16 - s32
                        f.write(pattern)
































