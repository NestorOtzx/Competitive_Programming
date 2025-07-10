from sys import stdin

def min_covering_fail(A, L, H):
    A.sort()
    lans, ans, ok = [], 0, True
    n, N, l = 0, len(A), L
    while n < N and l < H and ok:
        if A[n][0] > l: ok = False

        best, n = n, n + 1
        while ok and n < N and A[n][0] <= l:
            if A[n][1] > A[best][1]: best = n
            n += 1
        l = A[best][1]
        ans += 1
    if not ok or l < H:
        ans = len(A)+1
    return ans

def solve(A, end):
    print(len(A)-min_covering_fail(A, 0, end))

def main():
    L, G = map(int, stdin.readline().split())
    while L + G > 0:
        A = []
        for g in range(G):
            x, r = map(int, stdin.readline().split())
            A.append((x-r, x+r))
        solve(A, L)
        L, G = map(int, stdin.readline().split())
main()

"""
40 3
5 5
20 10
40 10
40 5
5 5
11 8
20 10
30 3
40 10
40 5
0 10
10 10
20 10
30 10
40 10
40 3
10 10
18 10
25 10
40 3
10 10
18 10
25 15
0 0
"""
