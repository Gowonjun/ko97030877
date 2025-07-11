# 26198 Chronogram

T = int(input())
for i in range(T) :
    cnt = 0
    s = input()
    cnt += s.count('I')
    cnt += s.count('V') * 5
    cnt += s.count('X') * 10
    cnt += s.count('L') * 50
    cnt += s.count('C') * 100
    cnt += s.count('D') * 500
    cnt += s.count('M') * 1000
    print(cnt)