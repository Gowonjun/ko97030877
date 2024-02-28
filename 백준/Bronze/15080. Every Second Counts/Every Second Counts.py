h, m, s = map(int, input().split(":"))
t1 = h * 3600 + m * 60 + s

h, m, s = map(int, input().split(":"))
t2 = h * 3600 + m * 60 + s

if t2 < t1 :
    t2 += 3600 * 24
print(t2 - t1)