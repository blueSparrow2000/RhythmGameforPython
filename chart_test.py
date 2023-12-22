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

class Chart_Test():
    def __init__(self):
        self.song_name = 'test'

    def build_chart(self,full_path):

        ##################################### fill in
        song_length = 8 * 1000
        song_bpm = 100
        song_mpb = ((1000 * 60 / song_bpm))
        song_difficulty = -1
        number_of_nodes = 0
        total_points = 0
        recommended_fps = 60

        song_offset = 500
        ####################################

        with open("%s" % full_path, "w") as f:
            f.write('%d,%d,%d,%d,%d\n' % (song_length, song_bpm, song_difficulty, number_of_nodes,recommended_fps))

            ################################## fill in
            beat_pos = song_offset

            pattern = write_multi_tiles('NN__', beat_pos, ['1/','1/','',''])
            beat_pos += 1000
            f.write(pattern)

            pattern = write_multi_tiles('H_NN', beat_pos, ['1/300','','1/','1/'])
            beat_pos += 1000
            f.write(pattern)

            pattern = write_multi_tiles('HHHH', beat_pos, ['1/300','1/300','1/300','1/300'])
            beat_pos += 1000
            f.write(pattern)


            pattern = write_multi_tiles('HNHN', beat_pos, ['1/300','1/','1/300','1/'])
            beat_pos += 1000
            f.write(pattern)



            pattern = write_multi_tiles('NNNN', beat_pos, ['1/','1/','1/','1/'])
            beat_pos += 1000
            f.write(pattern)


            # pattern = write_multi_tiles('N___', beat_pos, ['1/','','',''])
            # beat_pos += 1000
            # f.write(pattern)


            pattern = write_multi_tiles('___N', beat_pos, ['','','','1/'])
            beat_pos += 1000
            f.write(pattern)


            pattern = write_multi_tiles('H___', beat_pos, ['1/1000','','',''])
            beat_pos += 1000
            f.write(pattern)
            ##################################
