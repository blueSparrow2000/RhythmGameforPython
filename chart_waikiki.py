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

class Chart_Waikiki():
    def __init__(self):
        self.song_name = 'Waikiki'

    def build_chart(self,full_path):
        ##################################### fill in
        song_length = 196 * 1000
        song_bpm = 123
        cycle = 4
        song_mpb = ((1000 * 60 / song_bpm) / cycle)  # 215  # milli-seconds per beat
        song_difficulty = 1
        delete_unnessesary_node = 34
        number_of_nodes = int((song_length / 1000) * (song_bpm / 60)) - 4 -delete_unnessesary_node
        ####################################

        with open("%s" % full_path, "w") as f:
            f.write('%d,%d,%d,%d\n' % (song_length, song_bpm, song_difficulty, number_of_nodes))
            ################################## fill in
            beats = 0
            switch = True
            while number_of_nodes > 0:
                if beats % cycle == 1:
                    pattern = ''
                    if switch:
                        pattern = basic_strike(beats, song_mpb, 1, 1)
                        number_of_nodes -= 1
                    else:
                        pattern = basic_hold(beats, song_mpb, 2, 1, 500)
                        number_of_nodes -= 1
                    f.write(pattern)
                    switch = not switch
                beats += 1

            ##################################

