'''
Score

- saves the highest score for each songs in .txt file
- reads the score file and gets the hightest score of the current song with 'song_name'

'''
import os, sys
from variables import *

def update_score(song_name,score):
    global creater_mode
    if creater_mode:
        return # do not update score


    APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
    full_path = os.path.join(APP_FOLDER, 'scores.txt')

    # check if there exist score.txt. If not make one
    if os.path.isfile(full_path):
        pass
    else:
        f = open(full_path, "x")


    tokens = []
    # read the content of txt file
    with open(full_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        tokens = [line.split(',') for line in lines]

    # scores to int
    tokens = [[token[0],float(token[1])] for token in tokens]
    #print(tokens)

    song_score_exists = False
    update_flag = False
    # check whether score should be updated or not
    for token in tokens:
        if token[0] == song_name:
            song_score_exists = True
            if token[1] < score:
                update_flag = True # should be updated
                tokens.remove(token)

    # removed
    #print(tokens)

    # if no song name or should be updated, then add to the tokens list
    if not song_score_exists or update_flag:
        tokens.append([song_name,score])
        print("New high score!")
        print("Score updated for %s to %.2f" % (song_name, score))

    # write the content to txt file
    with open(full_path, "w") as f:
        for token in tokens:
            f.write("%s,%.2f\n"%(token[0],round(token[1],2)))




def fetch_highest_score(song_name):
    APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
    full_path = os.path.join(APP_FOLDER, 'scores.txt')

    # check if there exist score.txt
    if os.path.isfile(full_path):
        pass
    else:
        return 0 # no song has been played before!

    tokens = []
    # read the content of txt file
    with open(full_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        tokens = [line.split(',') for line in lines]


    # check whether the song exists or not
    for token in tokens:
        if token[0] == song_name:
            return float(token[1])

    # if song was not found, return 0 since the song was not played before
    return 0

# print(fetch_highest_score('Crystal'))
#
# update_score('Crystal',10.0)
#
# update_score('BadApple',100.0)
#
# update_score('Crystal',20.0)
#
# update_score('Crystal',15.0)
#
# print(fetch_highest_score('Crystal'))