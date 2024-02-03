n, A = map(int, input().split())
L = list(map(int, input().split()))
cnt = 0
for elem in L :
    cnt += elem // A
print(cnt)