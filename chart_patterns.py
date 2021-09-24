import pygame

def basic_strike(beats,song_mpb,line,point):
    return "%s,%d,%d,%d\n"%('node',beats*song_mpb,line,point)

def basic_hold(beats,song_mpb,line,point,length):  # here, length is in milliseconds
    return "%s,%d,%d,%d,%d\n"%('hold',beats*song_mpb,line,point,length)

def double_tap(beats,song_mpb,line,point,spacing): # spacing in milliseconds
    return "%s,%d,%d,%d\n"%('node',beats*song_mpb,line,point),"%s,%d,%d,%d\n"%('node',beats*song_mpb+spacing,line,point)

def simultaneous_2_tap(beats,song_mpb,line1,line2,point):
    return "%s,%d,%d,%d\n"%('node',beats*song_mpb,line1,point),"%s,%d,%d,%d\n"%('node',beats*song_mpb,line2,point)

def simultaneous_2_hold(beats,song_mpb,line1,line2,point,length):
    return "%s,%d,%d,%d,%d\n"%('hold',beats*song_mpb,line1,point,length),"%s,%d,%d,%d,%d\n"%('hold',beats*song_mpb,line2,point,length)

def ta_dac():
    pass


def ta_dada_tada():
    pass