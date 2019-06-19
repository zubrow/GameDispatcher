
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
line = input()
while line != "STOP settings":
    line = input()
    

grid = []

while True:
    next_input_must_be("START turn")
    W,H=  [int(val) for val in input().split()]
    grid = [list(input().strip()) for i in range(H)]
    next_input_must_be("STOP turn")
    print("START action")
    print(random.choice("UDLRUDLRUDLRB"))
    print("STOP action")
    