cnt_2 = 0
cnt_e = 0
n = int(input())
s = input()
for elem in s :
    if elem == '2' :
        cnt_2 += 1
    elif elem == 'e' :
        cnt_e += 1
if cnt_2 == cnt_e :
    print('yee')
elif cnt_2 > cnt_e :
    print('2')
else :
    print('e')