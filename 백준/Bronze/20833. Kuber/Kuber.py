N = int(input())

cnt = 1
hap = 0
while cnt <= N :
    hap += pow(cnt, 3)
    cnt += 1
print(hap)