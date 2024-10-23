N, M = map(int, input().split())
L = list(map(int, input().split()))
cnt = 1
for elem in L :
    cnt = cnt * elem
print(cnt % M)