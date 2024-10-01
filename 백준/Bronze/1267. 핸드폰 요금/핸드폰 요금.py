N = int(input())
L = list(map(int, input().split()))
Y = 0
M = 0
for i in range(N) :
    Y += (L[i] // 30 + 1) * 10
    M += (L[i] // 60 + 1) * 15
if Y < M :
    print('Y %d' % Y)
elif Y > M :
    print('M %d' % M)
else :
    print('Y M %d' % Y)