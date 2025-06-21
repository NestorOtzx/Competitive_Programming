from sys import stdin
import math


eps = 10e-6
c = []
T = -1

INF = float('inf')
NINF = float('-inf')

def margin(mid):
    mint = INF
    for i in range(len(c)-1):
        if (c[i][0] != 0 and c[i][1] != 0):
            mint = min(mint, (mid/c[i][0]) + ((T-mid)/c[i][1]))
    cheater = INF
    if (c[-1][0] != 0 and c[-1][1] != 0):
        cheater = (mid/c[-1][0]) + ((T-mid)/c[-1][1])
    #print(mint, cheater, mint-cheater)
    return mint-cheater
    
def solve(l, r):
    while abs(r-l) >= eps:
        trd = (r-l)/3
        lmid = l+trd
        rmid = r-trd
        ml, mlmid, mrmid, mr = margin(l),margin(lmid), margin(rmid), margin(r)
        if mlmid <= mrmid:
            l = lmid
        else:
            r = rmid
    return r
    

def main():
    global c, T
    data = stdin.readline().strip()
    L = []
    
    while len(data) > 0:
        T = int(data)
        N = int(stdin.readline().strip())
        c = []
        for n in range(N):
            cr, ck = map(float, stdin.readline().split())
            c.append((cr, ck))
        r = solve(0, T)
        #print(r)
        marg = margin(r)*3600
        time = -1
        
        if (not math.isnan(marg) and marg != INF and marg != NINF):
            time = round(marg)
        
        #print(time)
        if (time >= 0):
            print("The cheater can win by %d seconds with r = %.2fkm and k = %.2fkm."%(time,round(r,2), round(T-r,2)))
        else:
            print("The cheater cannot win.") 
        data = stdin.readline().strip()
        if (len(data) == 0):
            data = stdin.readline().strip()
    
main()

"""
100
3
-2.3 0
4 -5.6
23 23
100
3
10.0 40.0
20.0 30.0
15.0 35.0

100
3
10.0 40.0
20.0 30.0
15.0 25.0
84
4
43.0 46.9
10.3 30.1
9.8 78.2
51.8 7.4

The cheater can win by 1195 seconds with r = 84.00km and k = 0.00km.
"""
