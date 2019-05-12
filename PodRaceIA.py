
# -*- coding: Utf-8 -*- 
import sys
import random 
player = 1
NB_PODS = 3
WIDTH = 100
HEIGHT = 100
pods = []
walls = []
checkpoints = []


def next_input_must_be(value):
    if input() != value:
        print("expected input was '",value,"'", sep="")
        quit()

def read_dimensions(parts):
    global WIDTH
    global HEIGHT
    WIDTH = int(parts[1])
    HEIGHT = int(parts[2])


def read_nb_pods(parts):
    global NB_PODS
    NB_PODS = int(parts[1])
    

def read_list_of_circles(parts):
    nb = int(parts[1])
    l = []
    for i in range(nb):
        values = map(int, input().split())
        l.append({
            "x":values[0],
            "y":values[1],
            "radius":values[2],
            })

def read_walls(parts):
    global walls
    walls = read_list_of_circles(parts)

def read_checkpoints(parts):
    global checkpoints
    checkpoints = read_list_of_circles(parts)






settings = {
    "DIMENSIONS":read_dimensions,
    "WALLS":read_walls,
    "CHECKPOINTS":read_checkpoints,
    "NB_PODS":read_nb_pods
}

next_input_must_be("START player")
player = int(input())
next_input_must_be("STOP player")


next_input_must_be("START settings")
line = input()
while line != "STOP settings":
    parts = line.split()
    try :
        settings[parts[0]](parts)
    except Exception as e:
        print(e, file=sys.stderr)
    line = input()
    


turn = 1
while True:
    next_input_must_be("START turn %d"%(turn))
    end = "STOP turn %d"%(turn)
    pods = []
    line = input()
    while line != end:
        play,pod,x,y,vx,vy,direction, health = map(float, input().split())
        if play == player:
            pods.append({
                "x":x,
                "y":y,
                "vx":vx,
                "vy":vy,
                "dir":direction,
                "health":health
                }) 
        line = input()


    print("START action %d"%(turn))
    for i in range(NB_PODS):
        print(random.randint(-10,10),random.randint(3,10), end=";")
    print("")
    print("STOP action %d"%(turn))
    turn += 1
    