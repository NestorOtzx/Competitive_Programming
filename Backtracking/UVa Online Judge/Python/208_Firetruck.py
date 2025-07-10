from sys import stdin

MAX = 22
G = [[] for _ in range(MAX)]
Vis = [ False for _ in range(MAX)]
Np = [ False for _ in range(MAX)]
F = 0

counter = 0
def dfs(v):
    global Np
    if not Np[v]:
        Np[v] = True
        for u in G[v]:
            dfs(u)

def check(n):
    return not(Vis[n] or not Np[n])

def backtrack(n, cam):
    global Vis, counter
    
    if n == F:
        #print('', end = '')
        print(' '.join(map(str, cam)))
        counter += 1
    else:
        Vis[n] = True
        
        for u in G[n]:
            if check(u):
                nc = list(cam)
                nc.append(u)
                backtrack(u, nc)
        Vis[n] = False

def solve(case):
    global G, counter
    print("CASE %d:"%(case))
    backtrack(1, [1])
    print("There are %d routes from the firestation to streetcorner %d."%(counter, F))
    

def main():
    global G, Vis, Np, F, counter
    data = stdin.readline().strip()
    case = 1
    while len(data)>0:
        F = int(data)
        a, b = map(int, stdin.readline().split())
        Vis = [ False for _ in range(MAX)]
        Np = [ False for _ in range(MAX)]
        G = [[] for _ in range(MAX)]
        counter = 0
        while a + b != 0:
            G[a].append(b)
            G[b].append(a)
            a, b = map(int, stdin.readline().split())
        for i in range(len(G)):
            G[i].sort()
        dfs(F)
        solve(case)
        case += 1
        data = stdin.readline().strip()

main()

"""
6
1 2
1 3
3 4
3 5
4 6
5 6
2 3
2 4
0 0
4
2 3
3 4
5 1
1 6
7 8
8 9
2 5
5 7
3 1
1 8
4 6
6 9
0 0
"""
