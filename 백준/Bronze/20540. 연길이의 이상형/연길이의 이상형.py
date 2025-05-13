# 20540 연길이의 이상형

s = input()
if s[0] == 'I' :
    s = s.replace('I', 'E')
else :
    s = s.replace('E', 'I')
if s[1] == 'S' :
    s = s.replace('S', 'N')
else :
    s = s.replace('N', 'S')
if s[2] == 'T' :
    s = s.replace('T', 'F')
else :
    s = s.replace('F', 'T')
if s[3] == 'J' :
    s = s.replace('J', 'P')
else :
    s = s.replace('P', 'J')
print(s)