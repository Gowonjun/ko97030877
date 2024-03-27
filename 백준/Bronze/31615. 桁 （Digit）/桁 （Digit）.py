A = int(input())
B = int(input())
hap = A + B
res = hap / 10
if res < 1 :
    print(1)
if res >= 1 and res < 10 :
    print(2)
if res >= 10 and res < 100 :
    print(3)