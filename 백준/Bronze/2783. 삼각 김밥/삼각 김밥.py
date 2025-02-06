L = []
X, Y = map(int, input().split())
L.append(X / Y)
N = int(input())
for i in range(N) :
    X, Y = map(int, input().split())
    L.append(X / Y)
print(min(L) * 1000)