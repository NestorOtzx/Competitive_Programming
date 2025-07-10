from sys import stdin

Watts = [100, 9900, 990000, float('inf')]
Americus = [2, 3, 5, 7]

def Wh_to_americus(Wh):
    ans = 0
    i = 0
    while i < len(Watts):
        if Wh < Watts[i] and Wh >= 0:
            ans += Wh*Americus[i]
            Wh = 0
            i = len(Watts)
        else:
            ans += Americus[i]*Watts[i]
            Wh -= Watts[i]
        i+=1
    return ans

def Americus_to_Wh(Am):
    ans, i = 0, 0
    while i < len(Americus):
        if Am < Americus[i]*Watts[i] and Am >= 0:
            ans += Am // Americus[i]
            Am = 0
            i = len(Americus)
        else:
            ans += Watts[i]
            Am -= Americus[i]*Watts[i]
        i+=1
    return ans

#Que tan lejos esta pos de ser igual a B (con signo para simplificar la busqueda)
def DistB(B, Wh, pos): 
    a_yo = Wh_to_americus(pos)
    a_neigh = Wh_to_americus(Wh-pos)
    c = abs(a_yo-a_neigh)
    return c-B

def solve(A, B):
    Wh = Americus_to_Wh(A)
    low = 0
    hi = (Wh//2)+1 #yo no pago mas que ninguno de mis vecinos
    ans = -1
    while (low < hi):
        if (low + 1 == hi):
            if DistB(B, Wh, low) == 0:
                ans = Wh_to_americus(low)
            else:
                ans = Wh_to_americus(hi)
            low+=1
        else:
            mid = (low+hi)//2
            m = DistB(B, Wh, mid)
            if m > 0:
                low = mid
            else:
                hi = mid
    return ans

def main():
    A, B = list(map(int, stdin.readline().split()))
    while (A != 0 and B != 0):
        print(solve(A, B))
        A, B = list(map(int, stdin.readline().split()))
        
main()
        


"""
caso raro 1

458 58
respuesta: 162


"""
