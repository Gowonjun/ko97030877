s = input()
cntA = 0
cntB = 0
for i in range(len(s)) :
    if s[i] == 'A' :
        cntA += int(s[i + 1])
    elif s[i] == 'B' :
        cntB += int(s[i + 1])
if cntA > cntB :
    print('A')
else :
    print('B')