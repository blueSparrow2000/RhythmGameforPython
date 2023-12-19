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


def double_tap(pos,line,point,spacing): # spacing in milliseconds
    return "%s%s"%("%s,%d,%d,%d\n"%('node',pos,line,point),"%s,%d,%d,%d\n"%('node',pos+spacing,line,point))

def double_tap_to_left(pos,line,point,spacing): # spacing in milliseconds
    if line<=1:
        invalid("line must be bigger than 1")
    return "%s%s"%("%s,%d,%d,%d\n"%('node',pos,line,point),"%s,%d,%d,%d\n"%('node',pos+spacing,line-1,point))

def double_tap_to_right(pos,line,point,spacing): # spacing in milliseconds
    if line>=4:
        invalid("line must be smaller than 4")
    return "%s%s"%("%s,%d,%d,%d\n"%('node',pos,line,point),"%s,%d,%d,%d\n"%('node',pos+spacing,line+1,point))



def triple_tap(pos,line,point,spacing):
    return "%s%s%s"%("%s,%d,%d,%d\n"%('node',pos,line,point),"%s,%d,%d,%d\n"%('node',pos+spacing,line,point),"%s,%d,%d,%d\n"%('node',pos+2*spacing,line,point))

def triple_tap_to_left(pos,line,point,spacing):
    if line<=2:
        invalid("line must be bigger than 2")
    return "%s%s%s"%("%s,%d,%d,%d\n"%('node',pos,line,point),"%s,%d,%d,%d\n"%('node',pos+spacing,line-1,point),"%s,%d,%d,%d\n"%('node',pos+2*spacing,line-2,point))

def triple_tap_to_right(pos,line,point,spacing):
    if line>=3:
        invalid("line must be smaller than 3")
    return "%s%s%s"%("%s,%d,%d,%d\n"%('node',pos,line,point),"%s,%d,%d,%d\n"%('node',pos+spacing,line+1,point),"%s,%d,%d,%d\n"%('node',pos+2*spacing,line+2,point))


def triple_tap_lshift(pos,line,point,spacing):
    if line<=1:
        invalid("line must be bigger than 1")
    return "%s%s%s"%("%s,%d,%d,%d\n"%('node',pos,line,point),"%s,%d,%d,%d\n"%('node',pos+spacing,line-1,point),"%s,%d,%d,%d\n"%('node',pos+2*spacing,line,point))

def triple_tap_rshift(pos,line,point,spacing):
    if line>=4:
        invalid("line must be smaller than 4")
    return "%s%s%s"%("%s,%d,%d,%d\n"%('node',pos,line,point),"%s,%d,%d,%d\n"%('node',pos+spacing,line+1,point),"%s,%d,%d,%d\n"%('node',pos+2*spacing,line,point))



def quadro_tap_(pos,line,point,spacing):
    return "%s%s%s%s"%("%s,%d,%d,%d\n"%('node',pos,line,point),"%s,%d,%d,%d\n"%('node',pos+spacing,line,point),"%s,%d,%d,%d\n"%('node',pos+2*spacing,line,point),"%s,%d,%d,%d\n"%('node',pos+3*spacing,line,point))

def quadro_loscilate_(pos,line,point,spacing):
    if line<=1:
        invalid("line must be bigger than 1")
    return "%s%s%s%s"%("%s,%d,%d,%d\n"%('node',pos,line,point),"%s,%d,%d,%d\n"%('node',pos+spacing,line-1,point),"%s,%d,%d,%d\n"%('node',pos+2*spacing,line,point),"%s,%d,%d,%d\n"%('node',pos+3*spacing,line-1,point))

def quadro_roscilate_(pos,line,point,spacing):
    if line>=4:
        invalid("line must be smaller than 4")
    return "%s%s%s%s"%("%s,%d,%d,%d\n"%('node',pos,line,point),"%s,%d,%d,%d\n"%('node',pos+spacing,line+1,point),"%s,%d,%d,%d\n"%('node',pos+2*spacing,line,point),"%s,%d,%d,%d\n"%('node',pos+3*spacing,line+1,point))

def quadro_llinear_(pos,line,point,spacing):
    return "%s%s%s%s"%("%s,%d,%d,%d\n"%('node',pos,1,point),"%s,%d,%d,%d\n"%('node',pos+spacing,2,point),"%s,%d,%d,%d\n"%('node',pos+2*spacing,3,point),"%s,%d,%d,%d\n"%('node',pos+3*spacing,4,point))

def quadro_rlinear_(pos,line,point,spacing):
    return "%s%s%s%s"%("%s,%d,%d,%d\n"%('node',pos,4,point),"%s,%d,%d,%d\n"%('node',pos+spacing,3,point),"%s,%d,%d,%d\n"%('node',pos+2*spacing,2,point),"%s,%d,%d,%d\n"%('node',pos+3*spacing,1,point))




def simultaneous_2_tap(pos,line1,line2,point):
    return "%s%s"%("%s,%d,%d,%d\n"%('node',pos,line1,point),"%s,%d,%d,%d\n"%('node',pos,line2,point))

def simultaneous_2_hold(pos,line1,line2,point,length):
    return "%s%s"%("%s,%d,%d,%d,%d\n"%('hold',pos,line1,point,length),"%s,%d,%d,%d,%d\n"%('hold',pos,line2,point,length))
