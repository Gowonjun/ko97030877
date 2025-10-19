cnt = 0
N = int(input())
for i in range(N + 1) :
    for j in range(N + 1 - i) :
        cnt += 2 * i + j
print(cnt)