# 30314 Just a Joystick

n = int(input())
s = input()
ss = input()

cnt = 0 
for i in range(n) :
    if s[i] >= ss[i] :
        a = ord(ss[i]) + 26
        res = min(abs(ord(s[i]) - ord(ss[i])), a - ord(s[i]))
        #print(res)
        cnt += res
    else :
        a = ord(s[i]) + 26
        res = min(abs(ord(ss[i]) - ord(s[i])), a - ord(ss[i]))
        #print(res)
        cnt += res
print(cnt)