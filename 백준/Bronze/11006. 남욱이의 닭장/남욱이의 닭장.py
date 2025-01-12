# 11006 남욱이의 닭장

# 백업

T = int(input())

for i in range(T) :

    N, M = map(int, input().split())

    U = M * 2 - N

    T = M - U

    print(U, T)