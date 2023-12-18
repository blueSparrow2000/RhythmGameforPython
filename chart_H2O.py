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

class Chart_DropsOfH2O():
    def __init__(self):
        self.song_name = 'Drops of H2O'

    def build_chart(self,full_path):
        ##################################### fill in
        song_length = 98900
        song_bpm = 108*2
        cycle = 4
        song_mpb = ((1000 * 60 / song_bpm)/cycle)  # 215  # milli-seconds per beat
        song_difficulty = 0
        number_of_nodes = int((song_length / 1000) * (song_bpm / 60)) - 4

        song_offset = -230
        s1 = 108
        s2 = 54

        hold_len = 80
        ####################################

        with open("%s" % full_path, "w") as f:
            f.write('%d,%d,%d,%d\n' % (song_length, song_bpm, song_difficulty, number_of_nodes))
            ################################## fill in
            beat_pos = song_offset

            pattern = basic_hold(beat_pos, 4, 1, hold_len)
            beat_pos += s1
            #f.write(pattern)
            ##################################

