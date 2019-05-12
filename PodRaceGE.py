import sys
import math

visu = True
try : 
    import numpy as np
    import cv2
except Exception as e:
    print(e)
    visu = False

NB_PODS = 3
FRICTION = 0.005
WIDTH = 800
HEIGHT = 800


def next_input_must_be(value):
    val = input()
    if val != value:
        print("expected input was '%s' instead of '%s'"%(value, val))
        quit()



def prod(a,b):
    return [x*y for x,y in zip(a,b)]


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def get_arg(args, kwargs, pos, key, default):
    if pos < len(args):
        return args[pos]
    if key in kwargs:
        return kwargs[key]
    return default


class Element:
    def __init__(self,*args, **kwargs):
        self.x      = get_arg(args, kwargs, 0, "x",      0)
        self.y      = get_arg(args, kwargs, 1, "y",      0)
        self.radius = get_arg(args, kwargs, 2, "radius", 0)
        self.vx     = get_arg(args, kwargs, 3, "vx",     0)
        self.vy     = get_arg(args, kwargs, 4, "vy",     0)
        self.mass   = get_arg(args, kwargs, 5, "mass",   0)

    def get_velocity(self):
        return (self.vx, self.vy)

    def get_position(self):
        return (self.x, self.y)

    def collid_time(self, el):
        p1 = self.get_position()
        v1 = self.get_velocity()
        p2 = el.get_position()
        v2 = el.get_velocity()
        r1 = self.radius
        r2 = self.radius
        a = dot(v1,v1) + dot(v2,v2) - 2*dot(v1,v2)
        b = 2*(dot(p1,v1) + dot(p2,v2) - dot(p1,v2) - dot(p2,v1))
        c = dot(p1,p1) + dot(p2, p2) - 2*dot(p1,p2) - (r1+r2)**2
        delta = b**2-4*a*c
        if delta < 0 : return -1
        delta = delta**.5
        t1 = (- b - delta)/(2*a)
        t2 = (- b + delta)/(2*a)
        if t1 >= 0 : return t1
        return t2


    def intersect(self, el):
        p1 = self.get_position()

        
    def update_velocity(self, time, acc):
        self.vx += acc[0]*time
        self.vy += acc[1]*time

    def update_position(self, time):
        self.x += self.vx*time
        self.y += self.vy*time



class Pod(Element):
    def __init__(self, *args,**kwargs):
        Element.__init__(self,*args,**kwargs)
        self.direction = get_arg(args, kwargs, 6, "direction", 0)


    def turn(self, deg):
        self.direction+=deg

    def trust(self, power):
        angle = math.radians(self.direction)
        acc = (math.cos(angle)*power, math.sin(angle)*power)
        self.update_velocity( 1, acc)


    def friction(self, time):
        self.vx*=(1.0-FRICTION)**time
        self.vy*=(1.0-FRICTION)**time

def player_action(player, action):
    action = action.upper().split()


if visu:
    img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
    img[:, :] = [255, 255, 255]
    cv2.circle(img,(50, 100), 5, (0,255,0), -1)
    cv2.imshow('POD',img)
    cv2.waitKey(10)
walls = []




GE = True

if len(sys.argv) > 1 and sys.argv[1].lower() == "test":
    GE = False


if GE : 
    #read number of players
    next_input_must_be("START players")
    players = int(input())
    next_input_must_be("STOP players")
    print("START settings")
    print("NB_PODS",NB_PODS)
    print("STOP settings")

    #players position
    for i in range(1, players+1):
        x,y = find_random_free_case()
        grid[y][x] = str(i)
        player_position[i] = (x,y)




    turn = 1
    while True:
        winner = update_game()

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
        if visu :
            img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
            img[:, :] = [255, 255, 255]
            cv2.circle(img,(50, 100), 5, (0,255,0), -1)
            cv2.imshow('POD',img)
            cv2.waitKey(10)


else : 
    pod1 = Pod(400, 100, 10, 0.0,1, 1)
    pod2 = Pod(405, 500, 10, 1.0,-1, 1, -90)
    while True:
        pod1.friction(10)
        pod2.friction(10)
        pod1.update_position(10)
        pod2.update_position(10)
        pod1.trust(0.02)
        pod1.turn(10)

        pod2.trust(0.001)


        img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
        img[:, :] = [255, 255, 255]
        cv2.circle(img,(int(pod1.x), int(pod1.y)), pod1.radius, (0,255,0), -1)
        cv2.circle(img,(int(pod2.x), int(pod2.y)), pod2.radius, (255,255,0), -1)
        cv2.imshow('POD',img)
        k = cv2.waitKey(10)
        if k > 0 : break
