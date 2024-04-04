L = list(map(int, input().split()))
cnt = 0
for elem in L :
    if max(L) - elem <= 1000 :
        cnt += 1
print(cnt - 1)