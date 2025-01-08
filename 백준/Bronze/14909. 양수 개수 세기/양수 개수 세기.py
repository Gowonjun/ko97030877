# 14909 양수 개수 세기

# 백업

L = list(map(int, input().split()))

cnt = 0

for elem in L :

    if elem > 0 :

        cnt += 1

print(cnt)