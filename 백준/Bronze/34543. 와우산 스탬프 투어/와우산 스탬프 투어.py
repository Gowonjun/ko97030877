# 34543 와우산 스탬프 투어

N = int(input())
W = int(input())
hap = 0
hap += N * 10
if N >= 3 :
    hap += 20
if N == 5 :
    hap += 50
if W > 1000 :
    hap -= 15
if hap < 0 :
    hap = 0
print(hap)