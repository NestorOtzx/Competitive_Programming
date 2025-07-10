from collections import deque
from fractions import Fraction
from sys import stdin

G,name,code = list(),list(),dict()
costos = None

def encode(s):
    global name,code,G
    if s not in code:
        code[s] = len(code)
        name.append(s)
        G.append(list())
    return code[s]

def bfs(source, target):
    global vis, G
    vis = [False for _ in range(len(G))]
    bfsAux(source, target)
  
def bfsAux(u, target):
    global vis, costos, code
    q = deque()
    vis[u] = True
    q.append((u, 1, 1)) #vertice, costo1, costo2

    llegada = False
    while len(q) > 0 and not llegada:
        u = q.popleft()
        if (u[0] == target):
            llegada = True
            costos = (u[1], u[2])
        else:
            for vertice in G[u[0]]:
                if not vis[vertice[0]]:
                    vis[vertice[0]] = True
                    q.append((vertice[0], u[1]*vertice[1].denominator, u[2]*vertice[1].numerator))

def solve(source, target):
    global costos
    costos = None
    bfs(encode(source), encode(target))
    if (costos != None):
        frac = Fraction(costos[0], costos[1])
        print(f"{frac.numerator} {source} = {frac.denominator} {target}")
    else:
        print(f"? {source} = ? {target}")


def main():
    global G
    line = stdin.readline()
    while len(line)>2:
        tok = line.split()
        if tok[0][0]=='!':
            v0,c0,v1,c1 = int(tok[1]),encode(tok[2]),int(tok[4]),encode(tok[5])
            G[c0].append((c1, Fraction(v1, v0)))
            G[c1].append((c0, Fraction(v0, v1)))      
        else:
            ans = solve(tok[1], tok[3])
        line = stdin.readline()
    #print(G)
main()

