n = int(input())
k = int(input())

c = 0   # cheap
e = 0   # expensive

if (n - 60) >= k :
    print((k + 60) * 1500 + (n - 60 - k) * 3000)
elif (n - 60) < k :
    print(n * 1500)