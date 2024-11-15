# 17598 Animal King Election

cnt_L = 0
cnt_T = 0
for i in range(9) :
    s = input()
    if s == 'Lion' :
        cnt_L += 1
    elif s == 'Tiger' :
        cnt_T += 1
if cnt_L > cnt_T :
    print('Lion')
else :
    print('Tiger')