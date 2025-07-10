from sys import stdin

vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}

B1, B2 = [], []
words = set()
ans = list()
adding = True

def check(ind, vow, M, lword):
    ans = True
    if ind[0] > -1 and ind[1] > -1 and ind[0] < 4 and ind[1] < 4:
        letter = M[ind[0]][ind[1]] 
        if letter == None or (vow == 2 and letter in vowels) or (lword - vow == 2 and not letter in vowels):
            ans = False
    else:
        ans = False
    return ans 

def backtrack(i, j, vow, M, word):
    global words, ans
    if len(word) == 4:
        if adding: words.add(word)
        else:
            if word in words:
                ans.append(word)
                words.remove(word)
    else:
        indx = [(i+1, j),(i+1, j+1),(i+1, j-1),(i, j+1),(i, j-1),(i-1, j),(i-1, j+1),(i-1, j-1)]
        for ind in indx:
            if check(ind, vow, M, len(word)):
                vowl = vow
                letter = M[ind[0]][ind[1]] 
                if letter in vowels: vowl+=1
                M[ind[0]][ind[1]] = None
                backtrack(ind[0], ind[1], vowl, M, ''.join((word, letter)))
                M[ind[0]][ind[1]] = letter

            

def solve():
    global B1, B2, adding

    for i in range(4):
        for j in range(4):
            letter = B1[i][j]
            B1[i][j] = None
            vowl = 0
            if letter in vowels:
                vowl = 1
            backtrack(i,j,vowl,B1, ''.join(letter))
            B1[i][j] = letter
            
    adding = False

    for i in range(4):
        for j in range(4):
            letter = B2[i][j]
            B2[i][j] = None
            vowl = 0
            if letter in vowels:
                vowl = 1
            backtrack(i,j,vowl,B2, ''.join(letter))
            B2[i][j] = letter
    if len(ans) == 0:
        print("There are no common words for this pair of boggle boards.")
    else:
        ans.sort()
        for a in ans:
            print(a)
    

def main():
    global B1, B2, words, ans, adding
    data = stdin.readline().strip()
    while data != "#":
        B1 = [[] for _ in range(4)]
        B2 = [[] for _ in range(4)]
        words = set()
        ans = list()
        adding = True
        for i in range(4):
            data = data.split()
            B1[i], B2[i] = data[0:4], data[4:8]
            data = stdin.readline().strip()        
        solve()
        data = stdin.readline().strip()
        if data != "#":
            print("")
main()


"""
Z W A V  G S F U
U N C O  A H F T
Y T G I  G N A L
H G P M  B O O B

#

D F F B  W A S U
T U G I  B R E T
O K J M  Y A P Q
K M B E  L O Y R

Z W A V  G S F U
U N C O  A H F T
Y T G I  G N A L
H G P M  B O O B

#

"""
