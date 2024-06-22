cnt_even = 0
cnt_odd = 0
N = int(input())
K = input()
for elem in K :
    if int(elem) % 2 == 0 :
        cnt_even += 1
    else :
        cnt_odd += 1
if cnt_even > cnt_odd :
    print(0)
elif cnt_even < cnt_odd :
    print(1)
else :
    print(-1)