L = []
N = int(input())
for i in range(N) :
    a, b = map(int, input().split())
    if a <= b :
        L.append(b)
if len(L) == 0 :
    print(-1)
else :
    print(min(L))