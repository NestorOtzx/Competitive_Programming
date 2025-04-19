from sys import stdin


memo = dict()

def rec(n):
    global memo
    ans = 1
    if n in memo:
        ans = memo[n]
    else:
        if n != 1:
            if (n%2 == 0):
                ans = 1+ rec(n//2)
            else:
                ans = 1+ rec(3*n+1)
        memo[n] = ans
    return ans
    
def solve(i,j):
    ans = float('-inf')
    if i > j: i,j = j,i
    for n in range(i, j+1):
        ans = max(ans, rec(n))
    return ans

def main():
    global memo
    data = stdin.readline().strip()
    while len(data) > 0:
        i, j = map(int, data.split())
        
        print(i,j, solve(i,j))
        data = stdin.readline().strip()    
    

main()


"""
10 1
100 200
201 210
900 1000
"""
