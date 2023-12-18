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
        cycle = 4
        song_mpbq = ((1000 * 60 / song_bpm) / cycle)  # 215  # milli-seconds per beat
        song_difficulty = 1
        number_of_nodes = int((song_length / 1000) * (song_bpm / 60)) - 4
        total_points = 7

        song_offset = -500
        ####################################

        with open("%s" % full_path, "w") as f:
            f.write('%d,%d,%d,%d\n' % (song_length, song_bpm, song_difficulty, total_points ))

            ################################## fill in
            beat_pos = song_offset
            pattern = basic_hold(beat_pos , 1, total_points, 1000*(total_points))
            total_points -= total_points
            f.write(pattern)
            ##################################
