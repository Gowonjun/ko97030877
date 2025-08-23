# 2386  도비의 영어 공부

while True :
    s = input()
    if s == '#' :
        break
    else :
        a = s[0]
        s = s[2 : ]
        #print(s)
        #print(ord(a))
        b = chr(ord(a) - 32)
        #print(b)
        cnt = 0
        cnt += s.count(a)
        #print(s.count(a))
        cnt += s.count(b)
        #print(s.count(b))
        print(a, cnt)