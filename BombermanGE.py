import random 


WIDTH = 20
HEIGHT = 20

grid = []
player_position = {}
bombs = []

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
    x,y = player_position[player_id]
    grid[y][x] = '_'
    if action == 'U' and grid[y-1][x] == '_':
        y -= 1
    elif action == 'D' and grid[y+1][x] == '_':
        y += 1
    elif action == 'L' and grid[y][x-1] == '_':
        x -= 1
    elif action == 'R' and grid[y][x+1] == '_':
        x += 1
    grid[y][x] = str(player_id)
    player_position[player_id] = (x,y)





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


#players position
for i in range(1, players+1):
    x,y = find_random_free_case()
    grid[y][x] = str(i)
    player_position[i] = (x,y)




turn = 1
while True:
    for player in range(1,players+1):
        print("START turn %d %d"%(turn, player))
        print(WIDTH, HEIGHT)
        for gline in grid:
            print("".join(gline))
        print("STOP turn %d %d"%(turn, player))
        next_input_must_be("START actions %d %d"%(turn, player))
        action = input()
        player_action(player, action)
        next_input_must_be("STOP actions %d %d"%(turn, player))
    turn += 1



