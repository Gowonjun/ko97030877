d1, d2, d3 = map(int, input().split())
a = (d1 + d2 - d3) / 2
b = (d1 - d2 + d3) / 2
c = (-d1 + d2 + d3) / 2
if a <= 0 or b <= 0 or c <= 0 :
    print(-1)
else :
    print(1)
    print("%.1f %.1f %.1f" % (a, b, c))