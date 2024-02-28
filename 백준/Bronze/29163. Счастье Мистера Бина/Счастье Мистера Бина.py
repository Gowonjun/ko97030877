n = int(input())
L = list(map(int, input().split()))

cnt_odd, cnt_even = 0, 0
for elem in L :
    if elem % 2 == 0 :
        cnt_even += 1
    else :
        cnt_odd += 1
if cnt_even > cnt_odd :
    print('Happy')
else :
    print('Sad')