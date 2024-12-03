# 3058  짝수를 찾아라

T = int(input())
for _ in range(T) :
    LL = []
    L = list(map(int, input().split()))
    for elem in L :
        if elem % 2 == 0 :
            LL.append(elem)
    print(sum(LL), min(LL))