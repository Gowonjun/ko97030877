p1, p2, p3 = map(int, input().split())
a = p1 + p2 * 2 + p3 * 3
p1, p2, p3 = map(int, input().split())
b = p1 + p2 * 2 + p3 * 3
if a > b :
    print(1)
elif a < b :
    print(2)
else :
    print(0)