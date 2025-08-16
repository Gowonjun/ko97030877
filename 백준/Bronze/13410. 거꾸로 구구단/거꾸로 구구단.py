# 13410 거꾸로 구구단

N, K = map(int, input().split())
L = []
a = N
for i in range(K - 1) :
    a += N
    L.append(int(str(a)[::-1]))
print(max(L))