# -*- coding: Utf-8 -*- 
 
from tkinter import * 


def next_input_must_be(value):
    val = input()
    if val != value:
        print("expected input was '%s' instead of '%s'"%(value, val))
        quit()


grid = [["_"]*3 for x in range(3)]


for line in ["START players","2", "STOP players"]:
    next_input_must_be(line)

turn = 1
while True:
    for player in range(1,3):
        print("START turn %d %d"%(turn, player))
        for gline in grid:
            print("".join(gline))
        print("STOP turn %d %d"%(turn, player))
        next_input_must_be("START actions %d %d"%(turn, player))
        x,y = [int(x) for x in input().split()]
        if x in range(0,3) and y in range(0,3) and grid[y][x] == '_':
            grid[y][x] = str(player)
        next_input_must_be("STOP actions %d %d"%(turn, player))
    turn += 1



