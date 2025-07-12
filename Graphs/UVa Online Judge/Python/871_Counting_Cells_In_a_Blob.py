from sys import stdin
from collections import deque

G, vis = list(), list()

def bfs(x, y):
    global vis, G
    vis = [False for _ in range(len(G))]
    maxCuenta = 0
    for i in range(len(G)):
        if not vis[i] and G[i] != '0':
            cuentaActual = bfsAux(i, x, y)
            if (cuentaActual > maxCuenta):
                maxCuenta = cuentaActual
    return maxCuenta
    

def bfsAux(inicio, x, y):
    global vis,G
    q = deque()
    vis[inicio] = True
    q.append(inicio)
    cuenta = 0
    
    while len(q) > 0:
        cuenta+=1
        pos = q.popleft()
        dirs = []

        upPos = pos-x
        dwnPos = pos+x

        #limites izq y der
        yPos = pos//x
        l_limit = yPos*x
        r_limit = yPos*x+x

        #limites diagonales
        yupPos = (pos-x)//x
        lup_limit = yupPos*x
        rup_limit = yupPos*x+x
        ydwnPos = (pos+x)//x
        ldwn_limit = ydwnPos*x
        rdwn_limit = ydwnPos*x+x

        #DIRECCIONES
        if (pos-1 >= l_limit): #izq
            dirs.append(pos-1)
        if (pos+1 < r_limit): #der
            dirs.append(pos+1) 
        if (dwnPos < len(G)): #abajo
            dirs.append(pos+x)
        if (upPos >= 0): #arriba
            dirs.append(pos-x)

        #DIAGONALES
        if (upPos-1 >= 0 and upPos-1 > lup_limit-1): #up izq
            dirs.append(upPos-1)
        if (upPos+1 >= 0 and upPos+1 < l_limit): #up der
            dirs.append(upPos+1)
        if (dwnPos-1 < len(G) and dwnPos-1 > r_limit-1): #dwn izq
            dirs.append(dwnPos-1)
        if (dwnPos+1 < len(G) and dwnPos+1 < rdwn_limit): #dwn der
            dirs.append(dwnPos+1)

        #print("Visitando ", pos)
        #print("dir disponibles: ", dirs)
        for v in dirs:
            
            if not vis[v] and G[v] != '0':
                vis[v] = True
                q.append(v)
    return cuenta

def solve(x_tam, y_tam):
    global G
    print(bfs(x_tam, y_tam))

    
def main():
    global G
    linea = stdin.readline()
    casos = int(linea) 
    linea = stdin.readline() #linea en blanco
    for i in range(casos):
        w, h = 0, 0
        linea = stdin.readline() #primer fila
        w = len(linea)
        G.clear()
        while (len(linea)> 1): #resto de filas
            h+=1
            for c in linea:
                if (c != '\n'): G.append(c)
            linea = stdin.readline() #siguiente linea
        solve(w-1, h)
        if i < casos-1:
            print("")
main()

"""
1

0000
0010
0001
0110
"""
