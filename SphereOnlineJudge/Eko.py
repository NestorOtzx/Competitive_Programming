from sys import stdin

tres = []
M = 0

def check(mid):
    ans = 0
    for i in range(len(tres)):
        if mid <= tres[i]:
            ans += tres[i] - mid
    return ans
    

def phi(l,r):
    ans = 0
    if l+1 >= r:
        ans = l
    else:
        mid = int((l+r)//2)
        c = check(mid)
        if c < M:
            ans = phi(l, mid)
        else:
            ans = phi(mid, r)
    return ans
        


def main():
    global tres, M
    data = stdin.readline().strip()
    while len(data) > 0:
        N, M = map(int, data.split())
        tres = list(map(int, stdin.readline().split()))
        print(phi(0, max(tres)+1))
        data = stdin.readline().strip()

main()
