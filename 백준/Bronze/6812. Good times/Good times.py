# 6812  Good times

s = input()
if len(s) == 2 :
    h = 0
elif len(s) == 3 :
    h = int(s[0])
else :
    h = int(s[0 : 2])
m = s[-2] + s[-1]
hO = h
if hO == 0 :
    hO = ''
print(str(hO) + str(m), 'in Ottawa')
hV = (h - 3)
if hV < 0 :
    hV += 24
if hV == 0 :
    hV = ''
print(str(hV) + str(m), 'in Victoria')
hE = (h - 2)
if hE < 0 :
    hE += 24
if hE == 0 :
    hE = ''
print(str(hE) + str(m), 'in Edmonton')
hW = (h - 1)
if hW < 0 :
    hW += 24
if hW == 0 :
    hW = ''
print(str(hW) + str(m), 'in Winnipeg')
hT = h
if hT == 0 :
    hT = ''
print(str(hT) + str(m), 'in Toronto')
hH = h + 1
if hH >= 24 :
    hH -= 24
if hH == 0 :
    hH = ''
print(str(hH) + str(m), 'in Halifax')
hS = hH
m = int(m)
mS = m + 30
if mS >= 60 :
    hS += 1
    mS -= 60
if hS >= 24 :
    hS -= 24
if len(str(mS)) == 1 :
    mS = '0' + str(mS)
mS = str(mS)
if hS == 0 :
    hS = ''
print(str(hS) + mS, 'in St. John\'s')