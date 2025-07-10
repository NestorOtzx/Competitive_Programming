from sys import stdin
from collections import deque
from heapq import heappush, heappop

G,inc,name,code = list(),list(),list(),dict()


def encode(s):
    global name,code,G
    if s not in code:
        code[s] = len(code)
        name.append(s)
        G.append(list())
    return code[s]

def topoSort(G, inc):
    global name
    q, topo = [], ""
    for i in range(len(G)):
        if inc[i] == 0:
            heappush(q, i)

    while len(q) != 0:
        u = heappop(q)
        topo+=" "+name[u]

        for i in range(len(G[u])):
            v = G[u][i]
            inc[v] -= 1
            if inc[v] == 0:
                heappush(q, v)
    return topo

def solve(c):
    global G,inc
    strOrder = topoSort(G, inc)
    print(f"Case #{c}: Dilbert should drink beverages in this order:{strOrder}.")
    print("")

def main():
    global G, code, name, inc
    line = stdin.readline()

    c = 1
    while len(line) != 0:
        G,name,inc,code = list(),list(),list(),dict()

        if (line!= '\n'):
            n = int(line)
            for i in range(n):
                nombre = stdin.readline()
                encode(nombre.split("\n")[0])

            inc = [0 for _ in range(len(G))]
            
            line = stdin.readline()
            m = int(line)
            for j in range(m):
                line = stdin.readline().split()
                G[encode(line[0])].append(encode(line[1]))
                inc[encode(line[1])]+=1
                
            solve(c)
            c+=1
        
        line = stdin.readline()
        
main()

