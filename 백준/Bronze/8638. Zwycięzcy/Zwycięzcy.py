# 8638  Zwycięzcy

N = int(input())
L = list(map(int, input().split()))
s = ''
for i in range(N) :
    if L[i] == max(L) :
        s = s + chr(i + 65)
print(s)