# 5523  경기 결과

cntA, cntB = 0, 0
N = int(input())
for i in range(N) :
    A, B = map(int, input().split())
    if A > B :
        cntA += 1
    elif A < B :
        cntB += 1
print(cntA, cntB)