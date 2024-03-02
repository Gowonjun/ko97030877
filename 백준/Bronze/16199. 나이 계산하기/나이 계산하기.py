y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

yeon = y2 - y1
se = yeon + 1
man = yeon
'''
if m1 > m2 :
    man -= 1
elif d1 > d2 :
    man -= 1
'''
if m1 * 30 + d1 > m2 * 30 + d2 :
    man -= 1
# print("%d\n%d\n%d" % (man, se, yeon))
print(man)
print(se)
print(yeon)