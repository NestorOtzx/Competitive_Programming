from sys import stdin

B = [None]*102

N, R, C,F = None,None,None,None

def cprint(m1,m2,n,rt1,rt2,a):
    node = str(n)
    if n == 0: node = "I"
    if n == F: node = "F"
    print("n:",node,"R1:",m1, "R2:",m2, "rt1:",rt1,"rt2:",rt2,"cans:",a)

def dist(inda,indb):
    return abs((B[inda][0]-B[indb][0]))+abs((B[inda][1]-B[indb][1]))

memo = dict()

def phi(m1,m2,rt1,rt2):
    global memo
    if (m1,m2,rt1,rt2) in memo:
        ans = memo[(m1,m2,rt1,rt2)]
    else:
        if m1 == F and m2 == F:
            ans = 1
        else:
            if (m1 == F):
                cost = max(dist(m2, F)-rt2, 0)
                ans = cost + phi(m1,F,0,0)
            elif (m2 == F):
                cost = max(dist(m1, F)-rt1, 0)
                ans = cost + phi(F,m2,0,0)
            else:
                n = max(m1,m2)
                dm1=max(dist(m1, n+1)-rt1,0)
                dm2=max(dist(m2, n+1)-rt2,0)
                ans = min(dm1 + phi(n+1,m2,0,dm1+rt2), dm2+phi(m1,n+1,dm2+rt1,0))
        memo[(m1,m2,rt1,rt2)] = ans
    return ans

def main():
    global N, R, C, F, B, memo
    data = stdin.readline().strip()
    while len(data) > 0:
        R,C = map(int, data.split())
        N = int(stdin.readline())
        B[0] = (1,1)
        memo = dict()
        for n in range(1,N+1):
            a,b = map(int, stdin.readline().split())
            B[n] = (a,b)
        F = N+1
        B[F] = (R,C)
        print(phi(0,0,0,0))
        data = stdin.readline().strip()    
    
main()

"""
2 4
4
1 1
2 4
1 4
2 2
"""
