# 25527 Counting Peaks of Infection

while True :
    n = int(input())
    if n == 0 :
        break
    v = list(map(int, input().split()))
    hap = 0
    for i in range(1, n - 1) :
        #print(i)
        if max(v[i - 1], v[i], v[i + 1]) == v[i] :
            hap += 1
    print(hap)