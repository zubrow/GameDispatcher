import random 
import sys

WIDTH = 20
HEIGHT = 20
DELAY = 6
RADIUS = 5
BOMBS = 10
grid = []
player_position = {}
bombs = {}

def next_input_must_be(value):
    val = input()
    if val != value:
        print("expected input was '%s' instead of '%s'"%(value, val))
        quit()


def find_random_free_case():
    while True:
        x = random.randrange(len(grid[0]))    
        y = random.randrange(len(grid))    
        if grid[y][x] == '_':
            break
    return x,y


def player_action(player_id, action):
    if action == "NOACTION":
        return
    if player_id not in player_position:
        return
    x,y = player_position[player_id]
    bomb_mask = 0
    if grid[y][x] in '5678':
         grid[y][x] = 'o'
         bomb_mask = 4
    else:
        grid[y][x] = '_'
    
    if action == 'U' and grid[y-1][x] == '_':
        bomb_mask = 0
        y -= 1
    elif action == 'D' and grid[y+1][x] == '_':
        bomb_mask = 0
        y += 1
    elif action == 'L' and grid[y][x-1] == '_':
        bomb_mask = 0
        x -= 1
    elif action == 'R' and grid[y][x+1] == '_':
        bomb_mask = 0
        x += 1
    elif action == 'B' and  grid[y][x] == '_':
        bomb_mask = 4
        bombs[(x,y)]=DELAY

    grid[y][x] = str(player_id+bomb_mask)
    player_position[player_id] = (x,y)



def trigger_bomb(origin):
    x,y = origin
    del bombs[origin]
    grid[y][x] = '_'
    decals = [(1,0), (-1,0), (0,1), (0, -1)]
    for dx,dy in decals:
        for i in range(1,RADIUS+1):
            cx,cy = x+i*dx, y+i*dy
            if grid[cy][cx] in "5678":
                player_id = int(grid[cy][cx]) - 4
                grid[cy][cx] = '_'
                print("bomb",origin," : del",player_id,"dans",player_position, file=sys.stderr)
                del player_position[player_id]
                trigger_bomb((cx,cy))
            elif grid[cy][cx] in "1234":
                player_id = int(grid[cy][cx])
                grid[cy][cx] = '_'
                print("bomb",origin,": del",player_id,"dans",player_position, file=sys.stderr)
                del player_position[player_id]
            elif grid[cy][cx] == "B":
                grid[cy][cx] = '_'
                trigger_bomb((cx,cy))
            elif grid[cy][cx] == "#":
                break


def update_bombs():
    for k,v in list(bombs.items()):
        if v == 1:
            trigger_bomb(k)
        else:
            bombs[k] = v-1
    if len(player_position) == 1:
        return list(player_position)[0]
    if not player_position:
        return -1


#grid generation
grid = [["#"]*HEIGHT]+ \
        [["#"]+(["_"]*(WIDTH-2))+["#"] for x in range(HEIGHT-2)] +\
        [["#"]*HEIGHT]

for i in range(random.randrange((WIDTH*HEIGHT)//8)):
    x,y = find_random_free_case()
    grid[y][x] = '#'

#read number of players
next_input_must_be("START players")
players = int(input())
next_input_must_be("STOP players")
print("START settings")
print("NB_BOMBS",BOMBS)
print("BOMB_DURATION",DELAY)
print("BOMB_RADIUS",RADIUS)
print("STOP settings")

#players position
for i in range(1, players+1):
    x,y = find_random_free_case()
    grid[y][x] = str(i)
    player_position[i] = (x,y)




turn = 1
while True:
    winner = update_bombs()

    for player in range(1,players+1):
        print("START turn %d %d"%(turn, player))
        if winner:
            print("WINNER",winner)
        else:
            print(WIDTH, HEIGHT)
            for gline in grid:
                print("".join(gline))
        print("STOP turn %d %d"%(turn, player))
        next_input_must_be("START actions %d %d"%(turn, player))
        action = input()
        player_action(player, action)
        next_input_must_be("STOP actions %d %d"%(turn, player))
    if winner : 
        break
    turn += 1



