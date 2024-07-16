hap = 0
n = int(input())
for i in range(1, n + 1) :
    for j in range(1, i + 1) :
#        print(i, j)
        if i * j <= n and i >= j :
            hap += 1
#            print('*')
            
print(hap)