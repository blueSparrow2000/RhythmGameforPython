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

from chart_patterns import *

class Chart_AnotherWay():
    def __init__(self):
        self.song_name ='Another way'

    def build_chart(self,full_path):
        ##################################### fill in
        song_length = 39500
        song_bpm = 126 #83
        cycle = 4
        song_mpb = ((1000 * 60 / song_bpm) / cycle)  # 215  # milli-seconds per beat
        song_difficulty = 3
        number_of_nodes = 95 # 84 + 3 + 8

        song_offset = 3700
        s1 = 146 #146
        s2 = (s1//4)*3

        hold_len = s1*2
        hold_half = s1
        hold_full = s1*4
        ####################################

        with open("%s" % full_path, "w") as f:
            f.write('%d,%d,%d,%d\n' % (song_length, song_bpm, song_difficulty, number_of_nodes))
            ################################## fill in
            beat_pos = song_offset

            for i in range(14): # reduce this into half.... too hard and anoying # 32
                pattern = basic_strike(beat_pos, 1, 1)
                beat_pos += s1
                f.write(pattern)

                pattern = basic_strike(beat_pos+s2, 2, 1)
                beat_pos += 2*s1
                f.write(pattern)


                pattern = basic_strike(beat_pos, 3, 1)
                beat_pos += s1
                f.write(pattern)

                for i in range(1,4):
                    pattern = basic_strike(beat_pos, i, 1)
                    if i==3:
                        beat_pos += s1
                    else:
                        beat_pos += s2
                    f.write(pattern)


            pattern = basic_hold(beat_pos - s1, 4, 1, hold_len)
            beat_pos += hold_len
            f.write(pattern)


            beat_pos += hold_len*2



            pattern = basic_hold(beat_pos, 4, 1, hold_half)
            beat_pos += hold_len
            f.write(pattern)

            pattern = basic_hold(beat_pos, 4, 1, hold_half)
            beat_pos += hold_len
            f.write(pattern)

            beat_pos += 200 # error correction

            # for j in range(4):
            #     for i in range(4):
            #         pattern = basic_hold(beat_pos, i+1, 1, hold_full)
            #         beat_pos += hold_full + s1
            #         f.write(pattern)

            for j in range(4):
                pattern = basic_strike(beat_pos + s1*4, j + 1, 1)
                #pattern += basic_strike(beat_pos + s1 * 12, j+1, 1)
                pattern += basic_strike(beat_pos + s1 * 17, j+1, 1)
                beat_pos += (hold_full + s1)*4
                f.write(pattern)





            ##################################



