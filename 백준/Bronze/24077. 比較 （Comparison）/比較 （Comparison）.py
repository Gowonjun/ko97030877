# 24077 比較 (Comparison)

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
hap = 0
for a in A :
    for b in B :
        #print(a, ',', b)
        if a <= b :
            hap += 1
            #print('yes')
print(hap)