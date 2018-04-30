
# -*- coding: Utf-8 -*- 
 
import random 
player = 1


def next_input_must_be(value):
    if input() != value:
        print("expected input was '",value,"'", sep="")
        quit()

next_input_must_be("START player")
player = int(input())
next_input_must_be("STOP player")

grid = []

turn = 1
while True:
    next_input_must_be("START turn %d"%(turn))
    grid = [list(input().strip()) for i in range(3)]
    next_input_must_be("STOP turn %d"%(turn))
    while True:
        x,y = [random.randrange(0,3) for i in range(2)]    
        if grid[y][x] == '_':
            break
    print("START action %d"%(turn))
    print(x,y)
    print("STOP action %d"%(turn))
    turn += 1
    