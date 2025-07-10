from sys import stdin
from math import pi, pow

EPS = 1e-6
N, F, R = None, None, None

def is_ok(V, x):
    cnt, n = 0,0
    while cnt < F and n != N:
        cnt += int(V[n]/x)
        n += 1
    return cnt>=F

def solve():
    V = [pi * r * r for r in R]
    low, hi = 0.0,V[-1]+2*EPS
    while hi-low>=EPS:
        mid = (low+hi)/2
        if is_ok(V, mid): low = mid
        else: hi = mid
    return low

def main():
    global N,F,R
    tcnt = int(stdin.readline())
    while tcnt!=0:
        N,F = map(int, stdin.readline().split())
        R = [int(r) for r in stdin.readline().split()]
        F += 1; R.sort()
        print('{0:.4f}'.format(solve()))
        tcnt -= 1
main()
    
