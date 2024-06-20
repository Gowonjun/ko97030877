flag = 0
n = int(input())
L = []
for i in range(3) :
    L = list(map(int, input().split()))
    if 7 not in L :
        flag += 1
if flag > 0 :
    print(0)
else :
    print(777)