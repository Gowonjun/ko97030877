# 5607  問題 １

s1, s2 = 0, 0
n = int(input())
for _ in range(n) :
    a, b = map(int, input().split())
    if a > b :
        s1 += a + b
    elif a < b :
        s2 += a + b
    else :
        s1 += a
        s2 += b
print(s1, s2)