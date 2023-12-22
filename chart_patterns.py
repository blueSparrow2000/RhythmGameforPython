import pygame


def invalid(statement):
    print(statement)
    raise ValueError

def basic_strike(pos,line,point):
    return "%s,%d,%d,%d\n"%('node',pos,line,point)

def special_strike(pos,line,point,special):
    return "%s,%d,%d,%d,%s\n"%('node',pos,line,point,special)


def basic_hold(pos,line,point,length):  # here, length is in milliseconds
    return "%s,%d,%d,%d,%d\n"%('hold',pos,line,point,length)


def special_hold(pos,line,point,length,special):  # here, length is in milliseconds
    return "%s,%d,%d,%d,%d,%s\n"%('hold',pos,line,point,length,special)


def strike_double(pos,line1,line2,point):
    return

def strike_triple(pos,line1,line2,point):
    return


def hold_double(pos,line1,line2,point,length):
    return

