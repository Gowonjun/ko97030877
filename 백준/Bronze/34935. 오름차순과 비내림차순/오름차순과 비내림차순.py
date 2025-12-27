# 34935 오름차순과 비내림차순

flag = 1
N = int(input())
L = list(map(int, input().split()))
for i in range(N - 1) :
    if (L[i + 1] > L[i]) is not True :
        flag = 0
print(flag)