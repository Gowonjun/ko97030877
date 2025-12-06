# 23103 Academic Distance

N = int(input())
b_x, b_y = map(int, input().split())
hap = 0
a = b_x + b_y
for i in range(N - 1) :
    x, y = map(int, input().split())
    hap += abs(b_x - x) + abs(b_y - y)
    #print(hap)
    b_x = x
    b_y = y
print(hap)