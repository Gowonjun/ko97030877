# 14541 Speed Limit

while True :
    n = int(input())
    if n == -1 :
        break
    temp = 0
    miles = 0
    for i in range(n) :
        s, t = map(int, input().split())
        miles += s * (t - temp)
        temp = t 
    print('%d miles' % miles)