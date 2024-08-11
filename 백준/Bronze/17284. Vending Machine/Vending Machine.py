m = 5000    # m = money
L = list(map(int, input().split()))
for elem in L :
    if elem == 1 :
        m -= 500
    elif elem == 2 :
        m -= 800
    else :
        m -= 1000
print(m)