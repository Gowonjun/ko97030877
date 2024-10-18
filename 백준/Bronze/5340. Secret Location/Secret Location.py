# 5340  Secret Location

L = []
for _ in range(6) :
    s = input()
    if s[-1] == ' ' :
        s = s[:-1]
    L.append(len(s))


print("Latitude %d:%d:%d" % (L[0], L[1], L[2]))
print("Longitude %d:%d:%d" % (L[3], L[4], L[5]))