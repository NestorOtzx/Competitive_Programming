from sys import stdin, setrecursionlimit
from collections import deque

grid = []
P = tuple()
vis = []
ans = 0

def bfs(nodo):
    global ans, vis, grid
    vis[nodo[0]][nodo[1]] = True
    if grid[nodo[0]][nodo[1]] == 'G':
        ans+=1
    q = deque()   
    q.append(nodo)
    while len(q) > 0:
        u = q.popleft()
        x, y = u[0], u[1]
        #print("visiting: ", x, y)
        dirs = [ (x+1, y), (x, y+1), (x-1, y), (x,y-1)]
        fdirs = []
        trap = False
        for d in dirs:
            if vis[d[0]][d[1]] == False and grid[d[0]][d[1]] != '#' and grid[d[0]][d[1]] != 'T' and (grid[d[0]][d[1]] == '.' or grid[d[0]][d[1]] == 'G'):
                fdirs.append(d)
            if grid[d[0]][d[1]] == 'T':
                trap = True
                break
        if trap == False:
            for d in fdirs:
                vis[d[0]][d[1]] = True
                if grid[d[0]][d[1]] == 'G':
                    ans+=1
                q.append(d)



def main():
    global grid, P, vis, ans
    data = stdin.readline().strip()
    while len(data) > 0:
        W, H = map(int, data.split())
        ans = 0
        grid = []
        for h in range(H):
            line = stdin.readline().strip()
            grid.append([])
            for w in range(W):
                grid[-1].append(line[w])
                if line[w] == 'P':
                   P = (h,w)
        vis = [[False for _ in range(W)] for aux in range(H)]
        #print(grid)
        #print(vis)
        bfs(P)
        print(ans)
        data = stdin.readline().strip()    
        
main()

"""
7 4
#######
#P.GTG#
#..TGG#
#######
8 6
########
#...GTG#
#..PG.G#
#...G#G#
#..TG.G#
########
5 4
#####
#P###
#.G##
#####


"""
