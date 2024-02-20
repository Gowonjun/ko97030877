T = int(input())
L = list(map(int, input().split()))
cnt = 0
for elem in L :
    if T == elem :
        cnt += 1
print(cnt)