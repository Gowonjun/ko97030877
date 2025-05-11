# 5612  터널의 입구와 출구

n = int(input())
m = int(input())
flag = 0
Max = m
for _ in range(n) :
    a, b = map(int, input().split())
    m = m + a - b
    if m < 0 :
        flag = 1
    elif m > Max :
        Max = m
if flag == 0 :
    print(Max)
else :
    print(0)