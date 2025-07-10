from sys import stdin
INF = float('inf')
ans = -INF
S,D = 0,0

Y = [None for _ in range(12)]

def check(n, s):
    return n < 4 or s <= 0

def backtrack(n, ssum, ssum5):
    global ans
    if n == 12:
       ans = max(ans, ssum)
    else:
        s, d = ssum5+S, ssum5+D
        if n >= 5:
            s-=Y[n-5]
            d-=Y[n-5]
        if check(n, s):
            Y[n] = S
            backtrack(n+1, ssum+S, s)
        if check(n, d):
            Y[n] = D
            backtrack(n+1, ssum+D, d)

def solve():
    global ans
    ans = -INF
    backtrack(0, 0, 0)
    if ans > 0:
        print(ans)
    else:
        print("Deficit")
    
def main():
    global S, D
    data = stdin.readline()
    while len(data) > 0:
        S, D = map(int, data.split())
        D = -D
        solve()
        data = stdin.readline()
        
        

main()

"""
59 237
375 743
200000 849694
2500000 8000000
"""
