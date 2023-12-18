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

class Chart_Destructoid():
    def __init__(self):
        self.song_name = 'Destructoid'

    def build_chart(self,full_path):
        ##################################### fill in
        song_length = 94900
        song_bpm = 110*2
        song_mpb = ((1000 * 60 / song_bpm))
        song_difficulty = 0
        number_of_nodes = 3

        gap = 100
        ####################################

        with open("%s" % full_path, "w") as f:
            f.write('%d,%d,%d,%d\n' % (song_length, song_bpm, song_difficulty, number_of_nodes))
            ################################## fill in
            beats = 0

            pattern = basic_strike(beats, 1, 1)
            beats += gap
            f.write(pattern)
            pattern = basic_strike(beats, 1, 1)
            beats += gap
            f.write(pattern)
            pattern = basic_strike(beats, 1, 1)
            beats += gap
            f.write(pattern)
            ##################################

