# 10102 개표

V = int(input())
L = input()
cnt_A = 0
cnt_B = 0
for elem in L :
    if elem == 'A' :
        cnt_A += 1
    else :
        cnt_B += 1
if cnt_A > cnt_B :
    print('A')
elif cnt_A < cnt_B :
    print('B')
else :
    print('Tie')