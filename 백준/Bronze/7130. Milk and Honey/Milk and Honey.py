# 7130  Milk and Honey

M, H = map(int, input().split())
N = int(input())
hap = 0
for i in range(N) :
    C, B = map(int, input().split())
    hap += max(M * C, H * B)
print(hap)