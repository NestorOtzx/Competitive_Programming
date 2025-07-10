from sys import stdin
from sys import setrecursionlimit
from heapq import heappush, heappop

setrecursionlimit(10000) 

G, puntosAtaque, visitado, padre, low, t = list(), dict(), None, None, None, -1

class PuntoDeAtaque: 
    def __init__(self, estacion, pigeonValue):
        self.estacion = estacion
        self.pigeonValue = pigeonValue
    def __repr__(self):
        return "%d %d" % (self.estacion, self.pigeonValue)
    def __gt__(self, punto):
        if self.pigeonValue == punto.pigeonValue:
            return self.estacion > punto.estacion
        else:
            return self.pigeonValue < punto.pigeonValue

def tarjanAux(v):
    global G, visitado, low, padre, t, puntosAtaque
    t+=1
    visitado[v], low[v] = t, t
    for u in G[v]:
        if visitado[u] < 0:
            padre[u] = v
            tarjanAux(u)
            low[v] = min(low[v], low[u])
            if low[u] >= visitado[v]:
                puntosAtaque[v] += 1
        elif u != padre[v]:
            low[v] = min(low[v], visitado[u])

def solve(n, m):
    global G, visitado, low, padre, t, puntosAtaque
    puntosAtaque, visitado, padre, low = dict(), [-1 for _ in range(len(G))], [-1 for _ in range(len(G))], [-1 for _ in range(len(G))]
    
    for v in range(n):
        puntosAtaque[v] = 1
    puntosAtaque[0] = 0 # el padre del dfs principal al final se conectara con al menos 1, entonces, sus puntos iniciales seran 0 ya que despues se le sumara 1 al menos 1 vez
    
    tarjanAux(0) # como el grafo siempre es conexo, no hay nodos que debamos verificar despues de ejecutar el algoritmo de tarjan en 0
    
    stack = []
    for v in range(n): #agregar a la cola de prioridad
        p = PuntoDeAtaque(v, puntosAtaque[v])
        heappush(stack, p)

    i = m
    while len(stack) > 0 and i>0:
        print(heappop(stack))
        i-=1

def main():
    global G
    n, m = map(int, stdin.readline().split())
    while n+m>0:
        G = [list() for _ in range(n)]
        x, y = map(int, stdin.readline().split())
        while x+y>-1:
            G[x].append(y)
            G[y].append(x)
            x, y = map(int, stdin.readline().split())
        solve(n, m)
        print("")
        n, m = map(int, stdin.readline().split())
main()
