N = int(input())  
L = list(map(int, input().split()))
cnt = N
for i in range(N - 1) :
#    print(L[i], L[i + 1])
    if L[i] > L[i + 1] :
        cnt -= 1
print(cnt)