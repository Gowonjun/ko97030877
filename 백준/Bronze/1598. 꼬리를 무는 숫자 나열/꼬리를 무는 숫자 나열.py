# 1598  꼬리를 무는 숫자 나열

a, b = map(int, input().split())

if a % 4 == 0 and b % 4 == 0 :
    ns = 0 # north - south
elif a % 4 == 0 :
    ns = abs(4 - b % 4) # north - south
elif b % 4 == 0 :
    ns = abs(a % 4 - 4) # north - south
else :
    ns = abs(a % 4 - b % 4) # north - south

if a % 4 == 0 :
    a = (a // 4) - 1
else :
    a = a // 4
if b % 4 == 0 :
    b = (b // 4) - 1
else :
    b = b // 4
ew = abs(a - b) # east - west
#print('a :', a, ', b :', b)
#print('ew :', ew, ', ns :', ns)
print(ew + ns)