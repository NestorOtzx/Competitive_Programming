from sys import stdin,setrecursionlimit
setrecursionlimit(100000)

Z, X = None, None

memo = dict()

def phi(i, j):
    ans = None
    if (i,j) in memo:
        ans = memo[(i,j)]
    else:
        if j == 0:
            ans = 1
        elif i == 0 and j != 0 or j > i:
            ans = 0
        else:
            if Z[j-1] == X[i-1]:
                ans = phi(i-1, j-1) + phi(i-1,j)
            else:
                ans = phi(i-1, j)
        memo[(i,j)] = ans
    return ans
        
def main():
    global Z, X, memo
    T = int(stdin.readline())
    for t in range(T):
        memo = dict()
        X = stdin.readline()
        Z = stdin.readline()
        print(phi(len(X), len(Z)))
        
main()
