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



# 이제부턴 basic strike나 special strike 녀석들이 이 함수를 부른다! (이전 차트 빌더들이랑 호환되게 함. 앞으로는 이 함수만 쓸듯)
def write_multi_tiles(pattern, beat_pos,info):
    multitile_info = "%s,%d"%(pattern,beat_pos)

    for i in range(4): # for each lane (1~4)
        info = ''
        multitile_info += info
        pass

    return multitile_info
