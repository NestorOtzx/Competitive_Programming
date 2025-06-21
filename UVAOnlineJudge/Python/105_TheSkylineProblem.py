from sys import stdin

A = []


def solve(i, l):
    if i == len(A):
        pass
    else:
        if i % 2 == 0: #horizontal
            B = A[i]
            b = i
            j = i+1
            while j < len(A):
                if B[0] <= A[j][2] and B[1] <= A[j][1]:
                    B = A[j]
                    b = j
                else:
                    break
                j+=1
            if B == A[i]:
                if j+1 < len(A):
                    B = A[j+1]
            if A[i][2] < B[0]: #esta por fuera
                print(A[i][0])
                print(A[i][2])
                print(0)
                print(B[i][0])
                solve(i+1, B[i][0])
            else: #esta en colision
                
        else: #vertical
            pass


def main():
    data = stdin.readline().strip()
    A.append((0,0,0))
    while len(data) > 0:
        L, H, R = map(int, stdin.readline().split())
        A.append((L,H,R))
    print("(")
    
    print(")")


main()
