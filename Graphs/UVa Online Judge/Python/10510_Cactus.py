from sys import stdin,setrecursionlimit

setrecursionlimit(10000000)
MAX = 10002
G = [[] for i in range(MAX)]
visitados, completado = [0 for i in range(MAX)], [0 for i in range(MAX)]
sccInd = [-1 for i in range(MAX)]
n, t, numSCC = int(), 0, 0
pilaS, pilaP = [], []
cactus = True

def gabow():
    global numSCC
    for i in range(n):
        if visitados[i] == -1:
            gabowAux(i)

def gabowAux(v):
    global t, numSCC, cactus, completado
    t += 1
    visitados[v] = t
    pilaS.append(v)
    pilaP.append(v)
    completado[v] = 1

    i = 0
    while i<len(G[v]) and cactus:
        w = G[v][i]
        if visitados[w] == -1:
            gabowAux(w)
        elif completado[w] == 2: #si tiene forward edges, no es un cactus
            cactus = False
        elif sccInd[w] == -1:
            while visitados[pilaP[-1]] > visitados[w]:
                pilaP.pop()
        i+=1
    if v == pilaP[-1] and cactus:
        numSCC += 1
        if numSCC > 1: #si tiene más de un componente fuertemente conexo, el grafo no es fuertemente conexo
            cactus = False
        #print("SCC con indice %d: " % numSCC, end = '')
        while pilaS[-1] != v:
            a = pilaS.pop()
            #print("%d " % a, end = '')
            sccInd[a] = numSCC - 1
        a = pilaS.pop()
        #print("%d " % a)
        sccInd[a] = numSCC - 1
        pilaP.pop()
    completado[v] = 2

def solve():
    global G, visitados, cactus, numSCC
    gabow()
    if cactus:
        print("YES")
    else:
        print("NO")
        
def main():
    global G, visitados, cactus, n, t, numSCC, sccInd, completado
    casos = int(stdin.readline())
    c = 0
    while c < casos:
        n = int(stdin.readline())
        m = int(stdin.readline())

        t, numSCC = 0, 0
        cactus = True
        for i in range(n):
            completado[i] = visitados[i] = sccInd[i] = -1
            G[i] = []
      
        for _ in range(m):
            v, u = map(int, stdin.readline().split())
            G[v].append(u)
        solve()
        c+=1
                

main()



