
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

next_input_must_be("START settings")
next_input_must_be("STOP settings")
grid = []

while True:
    next_input_must_be("START turn")
    grid = [list(input().strip()) for i in range(3)]
    next_input_must_be("STOP turn")
    while True:
        x,y = [random.randrange(0,3) for i in range(2)]    
        if grid[y][x] == '_':
            break
    print("START action")
    print(x,y)
    print("STOP action")
    
