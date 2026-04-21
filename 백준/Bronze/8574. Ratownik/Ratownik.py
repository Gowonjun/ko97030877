# 8574  Ratownik

n, k, x, y = map(int, input().split())
cnt = 0

for _ in range(n) :
    xi, yi = map(int, input().split())
    if (xi - x) ** 2 + (yi - y) ** 2 > k ** 2 :
        cnt += 1
print(cnt)