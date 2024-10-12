from sys import stdin
from collections import deque

vis = []
L, R, C = 0, 0, 0
Map = []

def bfsAux(pos):
    global vis, L, R, C
    q = deque()
    z,y,x = pos
    vis[z][y][x] = True
    pred = [[[(-1, -1, -1) for _ in range(C)] for _ in range(R)] for _ in range(L)]
    q.append(pos)
    #print(vis)
    arrived = False
    z, y, x = 0, 0, 0
    while len(q) > 0 and not arrived:
        z, y, x = q.popleft()
        #print("visting %d %d %d" % (z, y, x))
        if Map[z][y][x] == 'E':
            arrived = True
        else:
            Ind = [(z, y, x-1), (z, y, x+1), (z, y-1, x), (z, y+1, x), (z-1, y, x),(z+1, y, x)]
            for k, j, i in Ind:
                if k > -1 and j > -1 and i > -1 and k < L and j < R and i < C and Map[k][j][i] != '#' and not vis[k][j][i]:
                    vis[k][j][i] = True
                    q.append((k, j, i))
                    pred[k][j][i] = (z, y, x)
    cost = 0
    if arrived:
        p = pred[z][y][x]
        while p != (-1, -1, -1):
            #print(p)
            k, j, i = pred[p[0]][p[1]][p[2]]
            p = (k, j, i)
            cost+=1
    return cost
def solve(start):
    global Map
    #print("xd")
    #print(Map, start)
    ans = bfsAux(start)
    if ans == 0:
        print("Trapped!")
    else:
        print("Escaped in %d minute(s)."%(ans))

def main():
    global vis, L, R, C, Map
    L, R, C = map(int, stdin.readline().split())
    
    while L > 0:
        S = (-1, -1, -1)
        Map = [[] for _ in range(L)]
        vis = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
        for l in range(L):
            for r in range(R):
                Map[l].append(stdin.readline().strip())
                start = Map[l][r].find('S')
                if S[0] < 0 and start > -1:
                    S = (l, r, start)
            stdin.readline()
        solve(S)
        L, R, C = map(int, stdin.readline().split())    
        
    

main()



"""

3 4 5
S....
.###.
.##..
###.#

#####
#####
##.##
##...

#####
#####
#.###
####E

1 3 3
S##
#E#
###

0 0 0


"""
