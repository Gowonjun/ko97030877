import sys

while True :
    #s = (sys.stdin.readline())
    s = input()
    if s == '0 0 0' :
        break
    else :
        M, A, B = map(int, s.split())
    t = round((B - A) * M * 3600 / (A * B))  # t = time(second)
    h = t // 3600
    t = t % 3600
    m = t // 60
    s = t % 60
    print('%01d:%02d:%02d' % (h, m, s))