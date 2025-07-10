from sys import stdin
from heapq import heappush, heappop
INF = float('inf')
MAX = 501
G = [[] for _ in range(MAX)]
F = [0 for _ in range (100)]
dist = [INF for _ in range(MAX)]
pqueue = list()

def dijkstra(s):
    global G, F, pqueue, dist
    while (len(pqueue) != 0):
        du, u = heappop(pqueue)
        if (dist[u] == du):
            dist[u] = du
            for v, duv in G[u]:
                if du+duv < dist[v]:
                    dist[v] = du+duv
                    heappush(pqueue, (dist[v], v))

def solve(n_est, n_nodos):
    global pqueue, F, dist
    
    pqueue = []
    for est in range(n_est):
        heappush(pqueue, (0, F[est]))
        dist[F[est]] = 0
        
    dijkstra(F[0])
    distCpy = dist.copy()

    mejorDistancia, mejorNodo = INF, 0
    
    for v in range(n_nodos):
        heappush(pqueue, (0, v))
        dist[v] = 0
        dijkstra(v)

        maxDist, maxNd = -1, 0
        for u in range(n_nodos):
            if (dist[u] > maxDist):
                maxDist = dist[u]
                maxNd = u

        if (maxDist < mejorDistancia):
            mejorDistancia = maxDist
            mejorNodo = v
        
        #print(f"{v}: {maxDist}, {maxNd}")
        #print(dist)
        dist = distCpy.copy()
    print(mejorNodo+1)
    

def main():
    global G, dist
    c = int(stdin.readline())
    stdin.readline()
    for caso in range(c):
        fst, casas = map(int, stdin.readline().split())

        for v in range(casas):
            G[v] = []
            dist[v] = INF

        for est in range(fst): #estaciones
            F[est] = int(stdin.readline())-1
            #print("estaciones: ",F[est])

        linea = stdin.readline().strip()
        while (len(linea) > 0):
            a, b, l = map(int, linea.split())
            G[a-1].append((b-1, l))
            G[b-1].append((a-1, l))
            #print(linea)
            
            linea = stdin.readline().strip()
        solve(fst, casas)
        if caso < c-1:
            print()
main()

"""
2

1 6
2
1 2 10
2 3 10
3 4 10
4 5 10
5 6 10
6 1 10

1 6
2
1 2 10
2 3 10
3 4 10
4 5 10
5 6 10
6 1 10

1

5 39
19
27
32
29
6
39 11 58
28 20 16
10 12 21
9 3 57
21 15 77
9 7 70
27 33 7
1 17 86
15 12 90
12 14 42
19 30 26
26 36 9
28 39 24
8 4 99
37 26 66
3 6 90
11 13 64
32 23 31
21 9 77
4 6 84
17 23 46
12 18 4
10 9 8
19 27 64
13 17 14
8 9 39
26 19 12
20 29 46
36 12 84
19 14 12
20 38 65
15 35 80
10 14 52
35 25 36
8 15 5
3 5 21
12 16 98
23 26 26
36 30 55
32 14 55
16 27 36
22 31 70
25 34 56
38 28 21
5 17 31
20 30 93
9 11 22
4 30 16
28 33 68
18 21 68
13 25 4
10 6 65
18 24 48
35 19 22
28 18 96
3 2 56
11 6 96
20 27 41
17 22 100
24 33 72
18 13 4
1 18 51
7 3 9
2 1 20
8 19 33
25 18 34
2 4 59
20 14 97
29 23 66
8 35 15
"""
