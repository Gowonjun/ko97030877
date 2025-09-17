# 4635  Speed Limit

while True :
    temp = 0
    hap = 0
    n = int(input())
    if n == -1 :
        break
    for i in range(n) :
        s, t = map(int, input().split())
        hap += s * (t - temp)
        temp = t
    print(hap, 'miles')