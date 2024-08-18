n = 0   # the number of people
m = 0   # m == max
for i in range(10) :
    a, b = map(int, input().split())
    if m < n :
        m = n
    n = n - a + b
print(m)