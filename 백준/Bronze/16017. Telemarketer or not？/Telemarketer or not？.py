cnt = 0

a = int(input())

if a != 8 and a != 9 :
    cnt += 1

b = int(input())
c = int(input())

if b != c :
    cnt += 1

d = int(input())

if d != 8 and d != 9 :
    cnt += 1

if cnt == 0 :
    print('ignore')
else :
    print('answer')