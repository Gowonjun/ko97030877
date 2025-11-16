# 15295 Chanukah Challenge

P = int(input())
for i in range(P) :
    K, N = map(int, input().split())
    a = (N * (1 + N)) // 2
    print(K, a + N)