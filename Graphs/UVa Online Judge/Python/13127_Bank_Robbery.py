from heapq import heappush,heappop
from sys import stdin
G, B, P = [], [], []

INF = float('inf')

def dijkstraMod(S): 
  global G
  dist = [ INF ]*len(G) ;
  pred = [-1] * len(G)
  pqueue = list()
  for s in S:
      dist[s] = 0
      heappush(pqueue, (dist[s], s))
  
  while len(pqueue)!=0:
    du,u = heappop(pqueue)
    if dist[u] == du:
      for v,duv in G[u]:
        if du+duv<dist[v]:
          dist[v] = du+duv
          pred[v] = u
          heappush(pqueue, (dist[v], v))
  return dist

def solve():
    global G, B, P
    dists = dijkstraMod(P) 
    maxB = -INF
    count = 0
    banks = []
    for b in B:
        maxB = max(maxB, dists[b])
    for b in B:
        if dists[b] == maxB:
            count+=1
            banks.append(b)
    if maxB == INF: print(count, "*")
    else: print(count, maxB)
    banks.sort()
    for i in range(len(banks)):
        if i < len(banks)-1:print(banks[i], end = ' ')
        else:print(banks[i])
    

def main():
    global G, B, P
    data = stdin.readline()
    while len(data) > 3:
        N, M, b, p = map(int, data.split())
        G = [[] for _ in range(N)]
        P, B = [], []
        for m in range(M):
            u,v,t = map(int,stdin.readline().split())
            G[u].append((v,t))
            G[v].append((u,t))
        if b > 0: B = list(map(int,stdin.readline().split()))
        if p > 0: P = list(map(int,stdin.readline().split()))
        solve()
        data = stdin.readline()
        
main()
