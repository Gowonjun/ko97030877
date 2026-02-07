# 7782  Alien

n = int(input())
b1, b2 = map(int, input().split())
flag = 0

for _ in range(n) :
    lx, ly, hx, hy = map(int, input().split())
    if lx <= b1 and b1 <= hx and ly <= b2 and b2 <= hy :
        flag = 1
if flag == 1 :
    print('Yes')
else :
    print('No')