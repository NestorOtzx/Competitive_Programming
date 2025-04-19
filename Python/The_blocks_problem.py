from sys import stdin
from collections import deque


locations = dict()
world = []

#asume que a está al final del deque
def ret(a): #retorna a su posicion original
    global world, locations
    world[locations[a]].pop()
    world[a].append(a)
    locations[a] = a

def moveonto(a,b):
    global world, locations
    la,lb = locations[a], locations[b]
    while world[la][-1] != a:
        ret(world[la][-1])
    while world[lb][-1] != b:
        ret(world[lb][-1])
    world[la].pop()
    world[lb].append(a)
    locations[a] = lb

def moveover(a,b):
    global world, locations
    la,lb = locations[a], locations[b]
    while world[la][-1] != a:
        ret(world[la][-1])
    world[la].pop()
    world[lb].append(a)
    locations[a] = lb
    
def pileonto(a,b):
    global world, locations
    la,lb = locations[a], locations[b]
    tmp = deque([])
    while world[la][-1] != a:
        tmp.appendleft(world[la][-1])
        locations[world[la][-1]] = lb
        world[la].pop()
    while world[lb][-1] != b:
        ret(world[lb][-1])
    world[la].pop()
    world[lb].append(a)
    world[lb].extend(tmp)
    locations[a] = lb

def pileover(a,b):
    global world, locations
    la,lb = locations[a], locations[b]
    tmp = deque([])
    while world[la][-1] != a:
        tmp.appendleft(world[la][-1])
        locations[world[la][-1]] = lb
        world[la].pop()
    world[la].pop()
    world[lb].append(a)
    world[lb].extend(tmp)
    locations[a] = lb

def main():
    global N, world, locations
    data = stdin.readline().strip()
    while len(data) > 0:
        N = int(data)
        world = []
        locations = dict()
        for n in range(N):
            locations[n] = n
            world.append(deque([n]))
        com = stdin.readline().strip()
        while com[0] != 'q':
            opts = com.split()
            pa,pb = int(opts[1]), int(opts[3])
            if locations[pa] != locations[pb]:
                if opts[0][0] == 'm': 
                    if opts[2][1] == 'n':
                        moveonto(pa,pb)
                    else:
                        moveover(pa,pb)
                else:
                    if opts[2][1] == 'n':
                        pileonto(pa,pb)
                    else:
                        pileover(pa,pb)
            com = stdin.readline().strip()
        
        for n in range(N):
            print("%d:"%(n),end='')
            while world[n]:
                print(" %d"%(world[n][0]), end='')
                world[n].popleft()
            print()
        data = stdin.readline().strip()
main()

"""

10
move 9 onto 1
move 2 onto 9
move 5 onto 3
pile 9 onto 3
quit
10
move 9 onto 1
move 2 onto 9
move 5 onto 3
pile 9 onto 3
quit
"""
