from sys import stdin
from math import *
from decimal import Decimal, getcontext

def carrera(x, y):
    vueltasP1 = 0
    vueltasP2 = 0

    tiempoP1 = 0
    tiempoP2 = 0
    x = Decimal(x)
    y = Decimal(y)
    
    c = ceil(1/Decimal(1-x/y))
    
    vueltasP1=c
    tiempoP1=x*c

    vueltasP2 = tiempoP1/y
    ventaja = vueltasP1-vueltasP2

    print(vueltasP1)

def main():
    data = stdin.readline().strip()
    while len(data) > 1:
        X,Y = map(int, data.split())
        carrera(X,Y)
        data = stdin.readline().strip()
    
main()


"""
1 10
4 8
5 7
6875 7109
"""
