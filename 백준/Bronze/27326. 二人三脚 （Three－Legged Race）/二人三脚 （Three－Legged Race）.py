# 27326 二人三脚 (Three-Legged Race)

N = int(input())
A = list(map(int, input().split()))
for i in range(1, N + 1) :
    if A.count(i) == 1 :
        print(i)
        break