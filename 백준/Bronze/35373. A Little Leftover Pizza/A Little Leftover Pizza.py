# 35373 A Little Leftover Pizza

s, m, l = 0, 0, 0
res = 0
n = int(input())
for i in range(n) :
    a, b = input().split()
    b = int(b)
    if a == 'S' :
        s += b
    elif a == 'M' :
        m += b
    else :
        l += b
while True :
    if s > 0 :
        s -= 6
        res += 1
    else :
        break
while True :
    if m > 0 :
        m -= 8
        res += 1
    else :
        break
while True :
    if l > 0 :
        l -= 12
        res += 1
    else :
        break
print(res)