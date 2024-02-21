hap = 91
def inp() :
    a = int(input())
    return a
a = inp()
hap += a
b = inp()
hap += b * 3
c = inp()
hap += c
print('The 1-3-sum is', hap)