from sys import stdin, setrecursionlimit
setrecursionlimit(10000000)

G = []
vis = []
def dfs(n):
    global G, vis
    vis[n] = True
    ans = 0
    ansn = n
    for u,c in G[n]:
        if vis[u] == False:
            nx,cx = dfs(u)
            if cx+c >= ans:
                ans = cx+c
                ansn = nx
    return (ansn, ans)


def main():
    global G, vis
    data = stdin.readline()
    
    while len(data) > 1:
        G = [ [] for _ in range(10001)]
        vis = [ False for _ in range(10001)]
        ini = -1
        while len(data) > 1:
            u,v,c = map(int, data.strip().split())
            if ini == -1:
                ini = u
            G[u].append((v,c))
            G[v].append((u,c))
            data = stdin.readline()
        far, cost = dfs(ini)
        vis = [ False for _ in range(10001)]
        fst, ans = dfs(far)
        print(ans)
        if len(data) == 1:
            data = stdin.readline()
            
main()

"""

5 1 6
1 4 5
6 3 9
2 6 8
6 1 7

5 1 6
1 4 5
6 3 9
2 6 8
6 1 7

"""


