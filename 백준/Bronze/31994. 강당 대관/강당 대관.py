cnt = 0
for i in range(7) :
    a, b = input().split()
    if int(b) > cnt :
        cnt = int(b)
        s = a
print(s)