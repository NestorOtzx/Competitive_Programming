from sys import stdin

def auxsplit(cad):
    words=[]
    word=""
    for i in range(len(cad)+1):
        
        if (i < len(cad)):
            #print(cad[i])
            if cad[i].isalpha():
                word += cad[i]
            elif len(word) > 0:
                words.append(word)
                word = ""
        elif len(word) > 0:
            words.append(word)
            word = ""        
    return words
    
def main():
    N = int(stdin.readline())
    for n in range(N):
        C = int(stdin.readline())
        cat = []
        
        for c in range(C):
            n, W, p = stdin.readline().strip().split()
            cat.append([n, int(p), set()])
        
            for w in range(int(W)):
                cat[c][2].add(stdin.readline().strip())
        line = stdin.readline().strip()
        while (len(line) > 0):
            #arr = line.split()
            arr = auxsplit(line)
            #print(arr)
            for word in arr:
                for i in range(len(cat)):
                    if word in cat[i][2]:
                        cat[i][1] -= 1
                        cat[i][2].remove(word)
            #print(cat)
            line = stdin.readline().strip()    

        ans = []
        for i in range(len(cat)):
            #print(cat[k])
            if cat[i][1] <= 0:
                ans.append(cat[i][0])
        if len(ans) == 0:
            print('SQF Problem.')
        else:
            print(','.join(ans))
            
main()  


"""
 a23 23 SQF problem nor a graph problem.
This is a bóäing geometrical problem. In this problem
you should calculate the convex area's of a regular polygon.




1
2
Graph 4 3
node
edge
directed
distance
Geometrical 4 2
point
convex
polygon
boring
This is neither


1
2
Graph 4 3
node
edge
directed
distance
Geometrical 4 2
point
convex
polygon
boring
This is neither a SQF problem nor a graph problem.
This is a boring. geometrical problem. In this problem
you should calculate the ''''convex''''¿'. area of a regular '''''polygon.

2
Graph 4 3
node
edge
directed
distance
Geometrical 4 2
point
convex
polygon
boring
node
node
node
node
"""
