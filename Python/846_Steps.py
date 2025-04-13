from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)

memo = dict()

def solve(x, y, step):
    global memo
    ans = None
    if (x,y,step) in memo:
        ans = memo[(x,y,step)]
    else:
        if x >= y:
            ans = 0
        elif x+step >= y:
            ans = 1
        else:
            ans = 2 + solve(x+step, y-step, step+1)
        memo[(x,y,step)] = ans
    return ans

def main():
    N = int(stdin.readline())
    for n in range(N):
        x, y = map(int, stdin.readline().split())
        print(solve(x, y, 1))
main()

"""
1
45 50
"""
