# 10406 The fellowship of the ring

W, N, P = map(int, input().split())
L = list(map(int, input().split()))
hap = 0
for elem in L :
    if elem >= W and elem <= N :
        hap += 1
print(hap)