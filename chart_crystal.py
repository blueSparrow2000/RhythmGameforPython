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

* hint
If you want to change to another song, just modify self.song_name, music_list.txt to the song you want to change!

'''

from chart_patterns import *

class Chart_Crystal():
    def __init__(self):
        self.song_name = 'Crystal'  #'Crystal_middle' # 'Crystal_climax'

    def build_chart(self,full_path):
        ##################################### fill in
        song_length = 101000
        song_bpm = 210 #140*2 #70
        song_mpb = ((1000 * 60 / song_bpm))  # 85.7
        song_difficulty = 4
        number_of_nodes = 211


        song_offset = -400

        hold_len1 = 2700
        hold_len2 = 1500
        hold_len3 = 800
        hold_gap = 100

        # middle settings
        s1 = 425
        s2 = s1//2 + 1
        s3 = s1//4

        #climax settings
        lsize0 = s3 - 50
        lsize1 = s2 - 50
        lsize2 = s1 - 50 # s2*2 -50
        lsize3 = s2*3 -50
        lsize4 = s1*2 -50
        ####################################



        with open("%s" % full_path, "w") as f:
            f.write('%d,%d,%d,%d\n' % (song_length, song_bpm, song_difficulty, number_of_nodes))
            ################################## phase 1
            beat_pos = song_offset

            # pattern = basic_strike(beat_pos, 1, 1)
            # beat_pos += s3
            # f.write(pattern)

            pattern = basic_hold(beat_pos, 1, 1, hold_len1)
            beat_pos += hold_len1
            f.write(pattern)

            pattern = basic_hold(beat_pos - 2*hold_gap, 2, 1, hold_len3+hold_gap)
            beat_pos += hold_len3
            f.write(pattern)

            pattern = basic_hold(beat_pos - 2*hold_gap, 3, 1, hold_len2+hold_gap)
            beat_pos += hold_len2
            f.write(pattern)

            pattern = basic_hold(beat_pos - 2*hold_gap, 2, 1, hold_len3+hold_gap)
            beat_pos += hold_len3
            f.write(pattern)

            pattern = basic_hold(beat_pos - 2*hold_gap, 1, 1, hold_len3+hold_gap)
            beat_pos += hold_len3
            f.write(pattern)

            pattern = basic_hold(beat_pos- hold_gap, 4, 1, hold_len1 + hold_gap)
            beat_pos += hold_len1
            f.write(pattern)

            pattern = basic_hold(beat_pos - hold_gap, 3, 1, hold_len3 + hold_gap)
            beat_pos += hold_len3
            f.write(pattern)

            pattern = basic_hold(beat_pos , 2, 1, hold_len1 + hold_gap)
            beat_pos += hold_len1
            f.write(pattern)

            pattern = basic_hold(beat_pos - hold_gap*2, 1, 1, hold_len3)
            beat_pos += hold_len3
            f.write(pattern)

            ##################################

            beat_pos -= 180 # error correction

            ############## phase 2 #########
            pattern = basic_strike(beat_pos -30, 4, 1)
            beat_pos += hold_len2 + hold_gap + 150
            f.write(pattern)

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += hold_len3
            f.write(pattern)

            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += hold_len3
            f.write(pattern)

            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += hold_len1
            f.write(pattern)

            beat_pos -= 80  # error correction

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += 80
            f.write(pattern)
            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += hold_len3//2 +10
            f.write(pattern)

            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += hold_len3//2
            f.write(pattern)

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += hold_len2
            f.write(pattern)


            beat_pos += 110 # error correction

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += hold_len3 + hold_gap
            f.write(pattern)

            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += hold_len3 + hold_gap
            f.write(pattern)


            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += hold_len2
            f.write(pattern)

            beat_pos += 140  # error correction

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += hold_len3 + hold_gap + 40
            f.write(pattern)

            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += hold_len3 + hold_gap + 40
            f.write(pattern)


            ##################################

            beat_pos -= 100  # error correction

            ############## phase 3 #########
            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += hold_len2 + hold_gap + 150
            f.write(pattern)

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += hold_len3
            f.write(pattern)

            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += hold_len3
            f.write(pattern)

            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += hold_len1
            f.write(pattern)

            beat_pos -= 80  # error correction


            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += 80
            f.write(pattern)
            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += hold_len3//2 +10
            f.write(pattern)

            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += hold_len3//2
            f.write(pattern)

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += hold_len2
            f.write(pattern)


            beat_pos += 110 # error correction

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += hold_len3 + hold_gap
            f.write(pattern)

            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += hold_len3 + hold_gap
            f.write(pattern)


            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += hold_len2
            f.write(pattern)

            beat_pos += 140  # error correction

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += hold_len3 + hold_gap + 40
            f.write(pattern)

            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += hold_gap*4
            f.write(pattern)

            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += 0
            f.write(pattern)

            ##################################


            beat_pos += s1 # error correction

            ######### middle part ################################################################################


            for i in range(4):
                pattern = basic_strike(beat_pos, 1, 1)
                beat_pos += s1
                f.write(pattern)

                pattern = basic_strike(beat_pos, 1, 1)
                beat_pos += s1
                f.write(pattern)

                pattern = basic_strike(beat_pos, 2, 1)
                beat_pos += s1
                f.write(pattern)

                pattern = basic_strike(beat_pos, 2, 1)
                beat_pos += s1
                f.write(pattern)

            beat_pos += 5

            for i in range(4):
                pattern = basic_strike(beat_pos, 1, 1)
                beat_pos += s2
                f.write(pattern)

                pattern = basic_strike(beat_pos, 2, 1)
                beat_pos += s2
                f.write(pattern)

                pattern = basic_strike(beat_pos, 1, 1)
                beat_pos += s2
                f.write(pattern)

                pattern = basic_strike(beat_pos, 2, 1)
                beat_pos += s2
                f.write(pattern)

            beat_pos += 5

            for i in range(4):
                pattern = basic_hold(beat_pos, 1, 1, s2)
                beat_pos += s1
                f.write(pattern)

                pattern = basic_hold(beat_pos, 2, 1, s2)
                beat_pos += s1
                f.write(pattern)

            ##################################

            ################################## Climax ####################################################################

            # climax offset

            #beat_pos += 10 # 343


            ########## type A ############ periodic
            for j in range(2):
                for i in range(2):
                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s1
                    f.write(pattern)

                    beat_pos += 10 # adjustments

                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s2
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s1
                    f.write(pattern)

                    beat_pos -= 10 # adjustments

                    for j in range(5):
                        pattern = basic_strike(beat_pos, 1, 1)
                        beat_pos += s2
                        f.write(pattern)

                        pattern = basic_strike(beat_pos, 2, 1)
                        beat_pos += s2
                        f.write(pattern)

                    #beat_pos -= 5
                beat_pos += 10


            ########## type B ####################################################################

            beat_pos += 10  # resting tempo

            for j in range(2):
                for i in range (4):
                    ########## type B-1 ############
                    pattern = basic_hold(beat_pos + s2, 2, 1, lsize2 - s2) # start late
                    beat_pos += s1
                    f.write(pattern)

                    pattern = basic_hold(beat_pos, 3, 1, lsize1)
                    beat_pos += s2
                    f.write(pattern)
                    pattern = basic_hold(beat_pos, 2, 1, lsize3)
                    beat_pos += s2*3
                    f.write(pattern)

                    if j==0:
                        pattern = basic_hold(beat_pos, 3, 1, lsize0)
                        beat_pos += s3
                        f.write(pattern)
                        pattern = basic_hold(beat_pos, 2, 1, lsize0)
                        beat_pos += s3
                        f.write(pattern)
                    else:
                        pattern = basic_hold(beat_pos, 2, 1, lsize0)
                        beat_pos += s3
                        f.write(pattern)

                    pattern = basic_hold(beat_pos, 3, 1, lsize1)
                    beat_pos += s2
                    f.write(pattern)

                    if i==0:
                        if j==1:
                            ############ type B-4 need fixes
                            pattern = basic_hold(beat_pos, 4, 1, lsize2)
                            beat_pos += s1
                            f.write(pattern)
                            pattern = basic_hold(beat_pos, 3, 1, lsize1)
                            beat_pos += s2
                            f.write(pattern)
                            pattern = basic_hold(beat_pos, 2, 1, lsize0)
                            beat_pos += s3
                            f.write(pattern)

                            pattern = basic_hold(beat_pos, 1, 1, lsize2)
                            beat_pos += s1
                            f.write(pattern)

                            pattern = basic_strike(beat_pos + 200, 2, 1)
                            beat_pos += s1
                            f.write(pattern)

                            # pattern = basic_hold(beat_pos, 2, 1, lsize1)  # arrive late
                            # beat_pos += s1
                            # f.write(pattern)

                            beat_pos -= 50  # error correction

                        else: # j==0
                            ############ type B-2
                            pattern = basic_hold(beat_pos+s2, 2, 1, lsize3-s2) # start late
                            beat_pos += s2*3
                            f.write(pattern)

                            pattern = basic_hold(beat_pos, 3, 1, lsize1)
                            beat_pos += s2
                            f.write(pattern)
                            pattern = basic_hold(beat_pos, 2, 1, lsize2)
                            beat_pos += s1
                            f.write(pattern)

                            pattern = basic_hold(beat_pos, 1, 1, lsize1)
                            beat_pos += s2
                            f.write(pattern)

                            pattern = basic_hold(beat_pos, 2, 1, lsize1)
                            beat_pos += s2
                            f.write(pattern)



                    elif i==1:
                        if j==1: # need extra adjustment
                            beat_pos += s3
                        ########## type B-3 ############
                        pattern = basic_hold(beat_pos, 2, 1, lsize4)
                        beat_pos += s1*2
                        f.write(pattern)

                        pattern = basic_hold(beat_pos, 3, 1, lsize3)
                        beat_pos += s2*3
                        f.write(pattern)
                        pattern = basic_hold(beat_pos, 4, 1, lsize1)
                        beat_pos += s2
                        f.write(pattern)


                    elif i==2:
                        beat_pos += s3  # error correction
                        if j==1:
                            beat_pos += s3  # error correction again!

                        pattern = basic_hold(beat_pos, 4, 1, lsize2)
                        beat_pos += s1
                        f.write(pattern)
                        pattern = basic_hold(beat_pos, 3, 1, lsize1)
                        beat_pos += s2
                        f.write(pattern)
                        pattern = basic_hold(beat_pos, 2, 1, lsize0)
                        beat_pos += s3
                        f.write(pattern)

                        pattern = basic_hold(beat_pos, 1, 1, lsize2)
                        beat_pos += s1
                        f.write(pattern)

                        pattern = basic_strike(beat_pos + 250, 2, 1)
                        beat_pos += s1
                        f.write(pattern)

                        # pattern = basic_hold(beat_pos, 2, 1, lsize1) # arrive late
                        # beat_pos += s1
                        # f.write(pattern)

                        beat_pos -= s3  # error correction

                    else:
                        beat_pos += 40  # start early

                        if j==1:
                            beat_pos += 200
                            ############ type B-6
                            pattern = basic_hold(beat_pos, 3, 1, lsize3 -s2)
                            beat_pos += s1
                            f.write(pattern)

                            pattern = basic_hold(beat_pos, 2, 1, lsize3)
                            beat_pos += s1
                            f.write(pattern)

                            pattern = basic_hold(beat_pos-s2, 1, 1, lsize4)
                            beat_pos += s2*3
                            f.write(pattern)

                            pattern = basic_hold(beat_pos + s3, 2, 1, lsize4)
                            beat_pos += 1000
                            f.write(pattern)

                        else:
                            pattern = basic_hold(beat_pos, 1, 1, lsize3)
                            beat_pos += s2*3
                            f.write(pattern)
                            pattern = basic_hold(beat_pos, 2, 1, lsize1)
                            beat_pos += s2
                            f.write(pattern)
                            pattern = basic_hold(beat_pos, 3, 1, lsize0)
                            beat_pos += s3
                            f.write(pattern)

                            pattern = basic_hold(beat_pos, 4, 1, lsize2)
                            beat_pos += s1
                            f.write(pattern)
                            pattern = basic_hold(beat_pos, 3, 1, lsize1)
                            beat_pos += s1
                            f.write(pattern)

                        beat_pos -= 40  # back to normal


                    beat_pos += 40  # resting tempo


        ##################################





