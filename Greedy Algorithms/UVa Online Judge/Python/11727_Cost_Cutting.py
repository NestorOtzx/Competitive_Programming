from sys import stdin
T = int(stdin.readline())
for t in range(T):
    l = list(map(int,stdin.readline().split()))
    l.sort()
    print("Case %d: %d"%(t+1,l[1]))
