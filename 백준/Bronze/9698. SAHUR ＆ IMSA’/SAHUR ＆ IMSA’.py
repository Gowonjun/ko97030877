T = int(input())
for i in range(1, T + 1) :
    H, M = map(int, input().split())
    H -= 1
    M += 60
    M -= 45
    if M >= 60 :
        H += 1
        M -= 60
    if H < 0 :
        H += 24
    print('Case #%d: %d %d' % (i, H, M))