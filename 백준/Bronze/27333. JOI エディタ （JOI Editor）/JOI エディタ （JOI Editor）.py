# 27333 JOI エディタ (JOI Editor)

N = int(input())
S = input()
S = S + '0'
s = ''
i = 0
while i < N :
    if S[i] == S[i + 1] :
        s = s + S[i].swapcase() * 2
        i += 2
    else :
        s = s + S[i]
        i += 1
print(s)