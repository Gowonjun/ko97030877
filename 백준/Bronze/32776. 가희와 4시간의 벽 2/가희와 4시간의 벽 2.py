# 32776 가희와 4시간의 벽 2

Sab = int(input())
Ma, Fab, Mb = map(int, (input().split()))
F = Ma + Fab + Mb

if Sab <= 240 :
    print('high speed rail')
elif Sab > F:
    print('flight')
else :
    print('high speed rail')