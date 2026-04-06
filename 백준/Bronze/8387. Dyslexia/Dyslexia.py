# 8387  Dyslexia

n = int(input())
s = input()
ss = input()
cnt = 0
for i in range(n) :
    if s[i] == ss[i] :
        cnt += 1
print(cnt)