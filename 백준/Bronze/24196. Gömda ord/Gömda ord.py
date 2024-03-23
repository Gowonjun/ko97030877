s = input()
ss = ''
cnt = 0
l = len(s)
while True :
    a = s[cnt]
    ss += a
    if l - 1 == cnt :
        break
    cnt += ord(a) - 64
print(ss)