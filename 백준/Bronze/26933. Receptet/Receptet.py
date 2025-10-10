# 26933 Receptet

hap = 0 
N = int(input())
for i in range(N) :
    H, B, K = map(int, input().split())
    if H < B :
        hap += (B - H) * K
print(hap)