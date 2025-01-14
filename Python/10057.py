from sys import stdin

INF = float('inf')
N, X = 0, list()

def ssum(mid):
    acum = 0
    for i in range(len(X)):
        acum += abs(X[i] - mid)
    return acum

def solve(low, hi):
    mins = INF
    while low + 1 < hi:
        
        mid = (low+hi)>>1
        print("low: ", low, "mid: ", mid, "hi: ", hi)
        s = ssum(mid)
        if s <= mins:
            hi = mid
            mins = s
        else:
            low = mid
    print("fin: low: ", low, "mid: ", mid, "hi: ", hi)
    print(low)

    


def main():
    global N, X
    data = stdin.readline().strip()
    while len(data) > 0:
        N = int(data)
        X = list()
        mini, maxi = INF, -INF
        for n in range(N):
            X.append(int(stdin.readline()))
            mini = min(mini, X[-1])
            maxi = max(maxi, X[-1])
        solve(mini, 2*maxi)
        data = stdin.readline().strip()
main()
