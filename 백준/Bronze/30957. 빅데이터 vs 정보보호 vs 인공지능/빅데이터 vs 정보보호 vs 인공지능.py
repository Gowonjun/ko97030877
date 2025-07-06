# 30957 빅데이터 vs 정보보호 vs 인공지능

N = int(input())
s = input()
cnt_B, cnt_S, cnt_A = 0, 0, 0
for i in range(N) :
    if s[i] == 'B' :
        cnt_B += 1
    elif s[i] == 'S' :
        cnt_S += 1
    else :
        cnt_A += 1
if cnt_B == cnt_S and cnt_B == cnt_A :
    print('SCU')
elif cnt_B > cnt_S and cnt_B > cnt_A :
    print('B')
elif cnt_S > cnt_B and cnt_S > cnt_A :
    print('S')
elif cnt_A > cnt_B and cnt_A > cnt_S :
    print('A')
else :
    if cnt_B < cnt_S and cnt_B < cnt_A and cnt_S == cnt_A :
        print('SA')
    elif cnt_S < cnt_B and cnt_S < cnt_A and cnt_B == cnt_A :
        print('BA')
    elif cnt_B == cnt_S and cnt_B > cnt_A and cnt_S > cnt_A :
        print('BS')