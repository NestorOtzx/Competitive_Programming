from sys import stdin
from math import log10

#funcion hecha viendo los patrones que tiene A[n] a medida que crece
def A(n):
    ans = 0
    if n % 4 == 0: ans= n
    else:
        if n%2 == 0: ans = n*10
        else: ans = (n*10)+2
    return ans

#potencias pre calculadas (lo hice para optimizar la potenciacion pero no era necesario)
POT = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, 100000000000000, 1000000000000000]

#count(n): calcula la cantidad de caracteres hasta un n.
#Todo esto surgio de un patron que vi para calcular las longitudes de las cadenas

#(cantidad de caracteres en la potencia de 10 mas cercana por la izquierda a n precalculada en base a observaciones)
PRECALC = [0, 16, 264, 3639, 46389, 563889, 6638889, 76388889, 863888889, 9638888889, 106388888889, 1163888888889, 12638888888889, 136388888888889, 1463888888888889, 15638888888888889]

#(cantidad de caracteres desde la potencia de 10 mas cercana hasta n)
#ej: res = (n-1000000)*8-((n-1000000)//4)

def count(n):
    ans = 0
    i = int(log10(n))
    ini = PRECALC[i]

    p = POT[i]
    res = (n-p)*(i+2)-((n-p)//4)
    ans = ini + res
    
    #condiciones especificas sobre ans
    if i == 1 and (n-1)%4 == 0: ans-=1 
    if i >= 2 and n%4 != 0: ans-=1
    return ans
    

def search(n): #busca la posicion en donde esta el numero en A usando la cantidad de caracteres como criterio
    ans = 0
    low = 0
    hi = POT[-1] #10**15
    while low < hi:
        if low+1== hi:
            ans = low
            low+=1
        else:
            mid = low + (hi-low)//2
            if count(mid) < n:
                low = mid
            else:
                hi = mid
    return ans

def solve(n):
    pos = search(n) #busqueda del indice de A donde esta el caracter n de la secuencia S
    charsbef = count(pos) #numero de caracteres antes de pos
    char = n-charsbef-1
    return(str(A(pos))[char])#retorna S[n]

def main():
    query = int(stdin.readline())
    while(query != 0):
        print(solve(query))
        query = int(stdin.readline())    
main()


"""
1
2
7
15
16
0
"""
