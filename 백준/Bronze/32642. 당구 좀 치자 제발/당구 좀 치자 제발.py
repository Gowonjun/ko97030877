# 32642 당구 좀 치자 제발

cnt = 0
hap = 0 # hap == sum
N = int(input())
L = list(map(int, input().split()))
for elem in L :
    if elem == 1 :
        cnt += 1
    else :
        cnt -= 1
    hap += cnt
print(hap)