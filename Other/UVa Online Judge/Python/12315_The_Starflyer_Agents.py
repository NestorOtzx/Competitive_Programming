#Nombre: Nestor Mauricio Ortiz Montenegro
#Codigo: 8972466
#Proyecto final: Análisis y diseño de algoritmos.
#Version con reemplazamiento extrictamente necesario que actualiza los reemplazamientos para evitar re calcularlos
#Mejor tiempo en UVA 1.470 s
from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)

CONST, FUNC, VAR = 0, 1, 2
SIZE = 20*(512//2)
#SIZE = 2000*(1000//2)
G, Nnames, Type, Remp = [ [] for _ in range(SIZE)], [ None for _ in range(SIZE)], [ None for _ in range(SIZE)], dict()
names = dict()

#Procedimiento que agrega al grafo G la representación como grafo del hash s a partir de l.
def makeTree(s, l):
    global G, Nnames,Type, names
    i,j, stack = 0,0, []
    last = l
    for x in range(len(s)):
        if s[x] in '(),':
            if j-i > 0:
                word = s[i:j]
                G[last] = list()
                if not word in names:
                    names[word] = len(names)
                #Nnames[last] = word #para depurar
                Nnames[last] = names[word] #para ejecutar
                Type[last] = CONST
                if s[i].isupper():
                    Type[last] = VAR
                if (len(stack) > 0):
                    G[stack[-1]].append(last)
                if s[x] == '(':
                    Type[last] = FUNC
                    stack.append(last)
                j+= 1
                i = j
                last+=1
            else:
                j+=1
                i+=1
            if s[x] == ')':
                stack.pop()
        else:
            j += 1
    if j-i > 0:
        word = s[i:j]
        G[last] = list()
        if not word in names:
            names[word] = len(names)
        #Nnames[last] = word #para depurar
        Nnames[last] = names[word] #para compilar
        if s[i].isupper():
            Type[last] = VAR
        else:
            Type[last] = CONST
        last+=1
    return last

#Función que decide si una variable var está dentro de un termino t o no.
def find(var, t):
    ans = False
    if Nnames[var] == Nnames[t]:
        ans = True
    elif Nnames[t] in Remp:
        ans = find(var, Remp[Nnames[t]])
    else:
        i = 0
        while i<len(G[t]) and ans == False:
            ans = find(var, G[t][i])
            i+=1
    return ans

#Funcion que realiza el reemplazamiento de una variable a hasta que ya no sea posible.
#Su valor de retorno indica el termino al que se llega cuando ya no es posible reemplazar más.
def rep(a):
    global Remp
    auxN = Nnames[a]
    t = Remp[Nnames[a]]
    Nnames[a] = Nnames[t]
    Type[a] = Type[t]
    G[a] = G[t]
    if Nnames[a] in Remp:
        ans = rep(a)
        Remp[auxN] = ans
    else:
        ans = t
    return ans
   
#Función que retorna verdadero si una lista de hashes L es unificable y falso si no lo es.
def unif(L):
    global Remp
    ans = True
    while len(L)>0 and ans:
        a, b = L.pop(), L.pop()
        if Nnames[a] in Remp:
            rep(a)
        if Nnames[b] in Remp:
            rep(b)
        if Type[a] != FUNC and Type[b] != FUNC and Nnames[a] == Nnames[b]:
            pass
        elif Type[a] == FUNC and Type[b] == FUNC and Nnames[a] == Nnames[b] and len(G[a]) == len(G[b]):
            for i in range(len(G[a])-1, -1, -1):
                L.append(G[b][i])
                L.append(G[a][i])
        elif Type[a] == VAR and not find(a, b):
            if not Nnames[a] in Remp:
                Remp[Nnames[a]] = b
        elif Type[b] == VAR and not find(b, a):
            if not Nnames[b] in Remp:
                Remp[Nnames[b]] = a
        else: ans = False
    return ans

#Calcula la respuesta al caso de prueba específico.
def solve(Ec, nomb):
    global Remp, names
    Remp = dict()
    L = [0]
    last = 0
    for i in range(len(Ec)-1, -1, -1):
        last = makeTree(Ec[i], last)
        if i > 0:
            L.append(last)
            if i > 1: L.append(last)
    ans = unif(L)
    if ans: print("analysis inconclusive on %s"%(nomb))
    else: print("%s is a Starflyer agent"%(nomb))
    
#Lectura de datos
def main():
    data = stdin.readline().split()
    while len(data) > 1 and data[1] != '0':
        nomb, N, T = data[0], int(data[1]), []
        for n in range(N):
            T.append(stdin.readline().strip())
        solve(T, nomb)
        data = stdin.readline().split()

main()

"""
r2d2 3
f(X,g(c))
f(f(Y),Z)
f(c,g(Y,d))
END 0

r2d2 3
f(X,g(c))
f(f(Y),Z)
f(c,g(Y,d))
c3po 2
f(X,g(c))
f(f(Y),Z)
PC2 2
f(f(Y),Z)
f(c,g(Y,d))
END 0
"""

