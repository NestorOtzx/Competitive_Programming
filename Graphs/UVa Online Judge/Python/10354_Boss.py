from sys import stdin
from sys import setrecursionlimit
from heapq import heappush, heappop

setrecursionlimit(10**6)

MAX = 101
G = [[] for _ in range(MAX)]
bossVisitado = [False for _ in range(MAX)]
p = -1
INF = float('inf')

def dijkstra(s, t, boss = False):
    global G, bossVisitado, p
    dist = [INF for _ in range(p)]
    antecesores = []
    
    pqueue = list()
    continuar = True

    dist[s] = 0
    heappush(pqueue, (0, s))
    
    while (len(pqueue) != 0 and continuar):
        du, u = heappop(pqueue)
        if (u == t):    
            if (boss):
                nodo = u
                while (nodo != None):                
                    for v, dv in G[nodo]:
                        if (dv+dist[v] == dist[nodo] and not bossVisitado[v]):
                            antecesores.append(v)
                    bossVisitado[nodo] = True
                    if (len(antecesores) > 0):
                        nodo = antecesores.pop()
                    else:
                        nodo = None                  
            continuar = False
        elif (dist[u] == du and not bossVisitado[u]):
            dist[u] = du
            for v, duv in G[u]:
                if du+duv < dist[v]:
                    dist[v] = du+duv
                    heappush(pqueue, (dist[v], v))
    return dist

def solve(bh, of, yh, m):
    global G, bossVisitado

    dists = dijkstra(bh, of, True)
    bossVisitado[of] = True
    bossVisitado[bh] = True
    
    if (bossVisitado[yh] or bossVisitado[m]):
        print("MISSION IMPOSSIBLE.")
    else:
        dists = dijkstra(yh, m, False)

        if (dists[m] == INF):
            print("MISSION IMPOSSIBLE.")
        else:
            print(dists[m])

def main():
    global G, p, bossVisitado
    linea = stdin.readline().split()
    while (len(linea) > 5):
        p, r, bh, of, yh, m= int(linea[0]), int(linea[1]), int(linea[2]), int(linea[3]), int(linea[4]), int(linea[5])

        for v in range(p):
            G[v] = []
            bossVisitado[v] = False
    
        for i in range(r):
            linea = stdin.readline().split()
            linea = [int(x) for x in linea]
            
            G[linea[0]-1].append((linea[1]-1, linea[2]))
            G[linea[1]-1].append((linea[0]-1, linea[2]))
        solve(bh-1, of-1, yh-1, m-1)
        
        linea = stdin.readline().split()

main()
