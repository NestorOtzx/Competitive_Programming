from sys import stdin

W,N = None,None
blocked = set()

def backtracking(i,j):
    global ans
    if i == W and j == N:
        ans+=1
    elif i <= W and j <= N:
        if not (i+1,j) in blocked:
            backtracking(i+1,j)
        if not (i,j+1) in blocked:
            backtracking(i,j+1)

def main():
    global W,N,blocked,ans
    T= int(stdin.readline())
    for t in range(T):
        stdin.readline()
        W,N = map(int,stdin.readline().split())
        blocked = set();
        ans = 0
        for w in range(W):
            l = list(map(int,stdin.readline().split()))
            for i in range(1, len(l)):
                blocked.add((l[0], l[i]))
        backtracking(1,1)
        print(ans)
        if (t<T-1):
            print()
main()
