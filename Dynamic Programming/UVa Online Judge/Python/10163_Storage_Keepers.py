from sys import stdin,setrecursionlimit
setrecursionlimit(1000000)
inf = float('inf')
P = list()
memo = dict()
memo1 = dict()
L = None

def phi(n, a):
    global memo
    ans, key = None, (n,a)
    if key in memo: ans = memo[key]
    else:
        if n == 0 and a != 0: ans = 0
        elif n == 0 and a == 0: ans = inf
        else:
            ans = phi(n-1, a)
            for k in range(1, min(a, P[n-1])+1):
                ans = max(ans, min(phi(n-1, a-k), P[n-1]//k))
        memo[key] = ans
    return ans

def ro(n,a):
    global memo1, L
    ans, key = None, (n,a)
    if key in memo1: ans = memo1[key]
    else:
        if n == 0 and a != 0: ans = inf
        elif n == 0 and a == 0: ans = 0
        else:
            ans = inf
            if phi(n-1, a) >= L:
                ans = min(ans, ro(n-1, a))
            for k in range(1, min(a, P[n-1])+1):
                if (P[n-1]//k) >= L and phi(n-1, a-k) >= L:
                    ans = min(ans, P[n-1] + ro(n-1, a-k))
        memo1[key] = ans
    return ans
            
def solve(a, M):
    global L
    L = phi(M, a)
    C = 0
    if L > 0:
        C = ro(M, a)
        
    print("%d %d"%(L, C))

def main():
    global P, memo,memo1
    data = list(map(int, stdin.readline().split()))
    while data[0] > 0:
        P = list(map(int, stdin.readline().split()))
        memo,memo1 = dict(),dict()
        solve(data[0], data[1])
        data = list(map(int, stdin.readline().split()))    

main()

"""
caso malo:
83 18
334 22 763 90 429 38 420 923 663 925 317 566 651 648 195 394 584 756 



2 1
7
1 2
10 9
2 5
10 8 6 4 1
5 4
1 1 1 1
0 0
"""
