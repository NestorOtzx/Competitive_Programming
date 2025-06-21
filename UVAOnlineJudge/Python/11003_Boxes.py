from sys import stdin

P = [0] * 1000
L = [0] * 1000

dp = [[0] * 6003 for _ in range(1001)]

def solve(N, ML):
    for n in range(N, -1, -1):
        for ml in range(0, ML + 1):
            if n == N:
                dp[n][ml] = 0
            else:
                if ml - P[n] >= 0:
                    dp[n][ml] = max(1 + dp[n + 1][min(ml - P[n], L[n])], dp[n + 1][ml])
                else:
                    dp[n][ml] = dp[n + 1][ml]
    return dp[0][6002]

def main():
    
    N = int(stdin.readline())
    while N != 0:
        for n in range(N):
            p, l = map(int, input().split())
            P[n] = p
            L[n] = l
        ans = solve(N, 6002)
        print(ans)
        N = int(stdin.readline())
        

main()
