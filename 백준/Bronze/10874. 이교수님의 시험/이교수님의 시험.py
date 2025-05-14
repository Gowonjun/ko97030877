# 10874 이교수님의 시험

N = int(input())
for i in range(1, N + 1) :
    flag = 0
    L = list(map(int, input().split()))
    for j in range(1, len(L) + 1) :
        if ((j - 1) % 5) + 1 != L[j - 1] :
            flag = 1
            break
    if flag == 0 :
        print(i)