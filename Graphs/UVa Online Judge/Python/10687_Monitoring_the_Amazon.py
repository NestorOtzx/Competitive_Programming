from sys import stdin
visitados = [False for _ in range(1000)]
puntos = [None for _ in range(1000)]
n = 0
n_visitados = 0

def dfsAux(nodo):
    global visitados, puntos, n, n_visitados
    visitados[nodo] = True
    n_visitados += 1
    puntos_cercanos = []
    for coord in range(n): #obtener puntos mas cercanos
        if coord != nodo:
            if len(puntos_cercanos)< 2:
                puntos_cercanos.append((coord, dist2puntos(puntos[nodo],puntos[coord])))
            else: #si hay mas de 2 nodos
                nuevoNodo = (coord, dist2puntos(puntos[nodo],puntos[coord]))
                i = 0
                while i<2:
                    if (nuevoNodo[1] < puntos_cercanos[i][1]): #si la distancia es menor
                        aux = puntos_cercanos[i]
                        puntos_cercanos[i] = nuevoNodo
                        nuevoNodo = aux
                    elif (puntos_cercanos[i][1] == nuevoNodo[1]):
                        c_Actual = puntos_cercanos[i][0]
                        c_Nueva = nuevoNodo[0]
                        if puntos[c_Nueva][0] < puntos[c_Actual][0]:
                            aux = puntos_cercanos[i]
                            puntos_cercanos[i] = nuevoNodo
                            nuevoNodo = aux
                        elif puntos[c_Nueva][0] == puntos[c_Actual][0]:
                            if puntos[c_Actual][1] >= puntos[c_Nueva][1]:
                                aux = puntos_cercanos[i]
                                puntos_cercanos[i] = nuevoNodo
                                nuevoNodo = aux
                    i+=1
    for n_nodo in range(len(puntos_cercanos)):
        if not visitados[puntos_cercanos[n_nodo][0]]:
            dfsAux(puntos_cercanos[n_nodo][0])

def dist2puntos(A,B):#la distancia al cuadrado entre 2 puntos
    return (A[0]-B[0])**2+(A[1]-B[1])**2

def main():
    global puntos, visitados, n, n_visitados
    linea = stdin.readline()
    n = int(linea) #n pares de enteros
    while (n != 0):
        linea = stdin.readline().split()
        n_visitados = 0
        for i in range(0, 2*n, 2):
            p = int(i/2)
            visitados[p] = False
            puntos[p] = (int(linea[i]), int(linea[i+1]))
            
        
        dfsAux(0)
        if (n == n_visitados):
            print("All stations are reachable.")
        else:
            print("There are stations that are unreachable.")
        linea = stdin.readline()
        n = int(linea) #n pares de enteros
main()
