from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10000)
MAX = 10000
G = [[] for i in range(MAX)]
visitado = [None for i in range(MAX)]
sccInd = [-1 for i in range(MAX)]
n, t, numSCC = int(), 0, 0
pilaS, pilaP = [], []

def gabow():
    global n
    ans = 1
    for i in range(n):
        sccInd[i], visitado[i] = -1, -1

    gabowAux(0)

    if numSCC>1:
        ans = 0
    else: #si despues del gabow algun elemento no fue visitado, quiere decir que no se puede llegar ahi por ningun camino
        for i in range(n):
            if visitado[i] == -1:
                ans = 0
    return ans

def gabowAux(v):
    global t, numSCC, G
    t+=1
    visitado[v] = t
    pilaS.append(v)
    pilaP.append(v)

    #detener el algoritmo cuando ya se sepa que hay al menos 2 componentes conexos
    i = 0
    while i<len(G[v]) and numSCC < 2:
        w = G[v][i]
        if visitado[w] == -1:
            gabowAux(w)
        elif sccInd[w] == -1:
            while visitado[pilaP[-1]] > visitado[w]:
                pilaP.pop()
        i+=1
    if v == pilaP[-1] and numSCC < 2:
        numSCC += 1
        pilaP.pop()
       
def solve(n):
    global G, sccNodos, numSCC
    print(gabow())

    
def main():
    global G, visitado, n, t, numSCC, pilaS, pilaP
    
    n, m = map(int, stdin.readline().split())
    while n+m>0:
        t, numSCC = 0, 0
        pilaS.clear()
        pilaP.clear()
        
        for x in range(n):
            G[x] = list()
            visitado[x] = False
        for x in range(m):
            v, w, p = map(int, stdin.readline().split())
            if p == 2:
                G[v-1].append(w-1)
                G[w-1].append(v-1)
            else:
                G[v-1].append(w-1)
        solve(n)
        n, m = map(int, stdin.readline().split())
main()
    
"""
4 5
1 2 1
1 3 2
2 4 1
3 4 1
4 1 2
3 2
1 2 2
1 3 2
3 2
1 2 2
1 3 1
4 2
1 2 2
3 4 2
0 0
"""
