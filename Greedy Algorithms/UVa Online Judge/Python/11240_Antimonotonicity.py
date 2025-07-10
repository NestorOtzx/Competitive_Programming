from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)

N = 0
F = []

def phi(n, prev):
    ans = None
    if n == N-1:
        ans = 1
    else:
        if prev < F[n] and F[n] <= F[n+1]:
            ans = phi(n+1, F[n])
        elif prev < F[n] and F[n] > F[n+1]:
            ans = 1+ phi(n+1, F[n])
        elif prev >= F[n] and F[n] <= F[n+1]:
            ans = 1+ phi(n+1, F[n])
        elif prev >= F[n] and F[n] > F[n+1]:
            ans = phi(n+1, F[n])
    return ans

def solve():
    print(phi(0, -float('inf')))

def main():
    global F, N
    T = int(stdin.readline())
    for t in range(T):
        data = stdin.readline().split()
        N = int(data[0])
        F = list(map(int, data[1:]))
        solve()
main()

"""
4
5 1 2 3 4 5
5 5 4 3 2 1
5 5 1 4 2 3
5 2 4 1 3 5
"""
