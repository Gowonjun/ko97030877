cnt_a, cnt_b = 100, 100
n = int(input())
for i in range(n) :
    a, b = map(int, input().split())
    if a > b :
        cnt_b -= a
    elif a < b :
        cnt_a -= b
print(cnt_a)
print(cnt_b)