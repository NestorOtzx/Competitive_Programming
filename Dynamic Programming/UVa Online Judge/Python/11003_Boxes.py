#too slow
from sys import stdin


P = [0] * 1000
L = [0] * 1000

memo = dict()
N = None

def solve(n, ml):
    ans = None
    if ((n,ml) in memo):
        ans = memo[(n,ml)]
    else:
        if n == N:
            ans= 0
        else:
            if ml - P[n] >= 0:
                ans = max(1 + solve(n + 1,min(ml - P[n], L[n])), solve(n + 1,ml))
            else:
                ans = solve(n+1,ml)
        memo[(n,ml)] = ans
    return ans

def main():
    global memo,N
    N = int(stdin.readline())
    while N != 0:
        memo = dict()
        for n in range(N):
            p, l = map(int, input().split())
            P[n] = p
            L[n] = l
        ans = solve(0, float('inf'))
        print(ans)
        N = int(stdin.readline())
        

main()
