from sys import stdin


def main():
    T = int(stdin.readline())
    for t in range(T):
        line = stdin.readline().strip()
        stack = []

        stack.append(line[0])
        ans = dict()
        for i in range(len(line)-1):
            if not stack[-1] in ans:
                ans[stack[-1]] = 0
            if i+1 < len(line):
                if (stack[-1] != line[i+1]):
                    stack.append(line[i+1])
                else:
                    if (len(stack)>1):
                        ans[stack[-1]]+=1
                    stack.pop()
                    if (len(stack)>0):
                        ans[stack[-1]]+=1
            #print(i)
            #print(ans)
            #print(stack)
        anso = list(ans)
        anso.sort()
        print("Case %d"%(t+1))
        for i in range(len(anso)):
            print("%c = %d"%(anso[i], ans[anso[i]]))
    

main()


"""

2
AEFFGGEBDDCCBA
ZAABBZ

"""
