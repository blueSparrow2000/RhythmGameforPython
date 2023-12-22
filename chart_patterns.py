import pygame


def invalid(statement):
    print(statement)
    raise ValueError

'''
pos: beat pos in ms
line: 1~4 
point: int
special: given as a string or not given
'''
def basic_strike(pos,line,point,special = ''):
    multi_line_pattern = ''
    info = []
    for i in range(1,5): # 1 to 4
        if i==line:
            multi_line_pattern += 'N'
            info.append('%d/%s'%(point,special))
        else:
            multi_line_pattern += '_'
            info.append('')

    return write_multi_tiles(multi_line_pattern, pos, info)

    #return "%s,%d,%d,%d,%s\n"%('node',pos,line,point,special)


'''
pos: beat pos in ms
line: 1~4 
point: int
length: hold length in ms
special: given as a string or not given
'''
def basic_hold(pos,line,point,length,special = ''):  # here, length is in milliseconds
    multi_line_pattern = ''
    info = []
    for i in range(1,5): # 1 to 4
        if i==line:
            multi_line_pattern += 'H'
            info.append('%d/%d/%s'%(point,length,special))
        else:
            multi_line_pattern += '_'
            info.append('')

    return write_multi_tiles(multi_line_pattern, pos, info)
    #return "%s,%d,%d,%d,%d\n"%('hold',pos,line,point,length)



# 이제부턴 basic strike나 special strike 녀석들이 이 함수를 부른다! (이전 차트 빌더들이랑 호환되게 함. 앞으로는 이 함수만 쓸듯)
# line 정보가 불필요. 패턴에 나와있고, 패턴을 통해 몇번 라인의 노드인지 홀드인지 다 알 수 있음
# info에는 포인트, (홀드의 경우, 길이),스페셜 유무 등이 들어감
# info is a list of length 4, each element is string: ['','1/BadApple','1/','1/100/'], each elem in the info should be separated by '/'
'''
Valid info elements:
'1/', '1' : Node with point 1, not special
'2/BadApple' : Node with point 2, special is BadApple
'1/100/', '1/100' : hold with point 1, length 100
'1/200/Debug' : Debug hold

'': No info. this is for '_' pattern. actually anything is fine since we ignore this place holder variable

Example of full arguement:
write_multi_tiles('N__H', beat_pos,['1/','','','1/300'])

'''
def write_multi_tiles(pattern, beat_pos,info):
    multi_tile_info = "%s,%d"%(pattern,beat_pos)

    for i in range(4): # for each lane (1~4)'s index 0 to 3
        tile_data = ',' #initialize data.
        tile_info = info[i].split('/')

        if pattern[i]=='_': # just add comma
            pass
        elif pattern[i]=='N':
            if len(tile_info) == 1: # this means not special. given only a number. add /
                info[i] += '/'
            tile_data += info[i]
        elif pattern[i]=='H':
            if len(tile_info) == 2: # this means not special. given only a number and length. add /
                info[i] += '/'
            tile_data += info[i]
        else:
            raise ValueError("Invalid pattern given!")

        multi_tile_info += tile_data

    return multi_tile_info+'\n'
