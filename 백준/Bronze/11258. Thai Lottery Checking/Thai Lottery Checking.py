# 11258 Thai Lottery Checking

all, all_prize = input().split()
f31, f31_prize = input().split()
f32, f32_prize = input().split()
b31, b31_prize = input().split()
b32, b32_prize = input().split()
b2, b2_prize = input().split()

while True :
    hap = 0
    n = input()
    if n == '-1' :
        break
    if all == n :
        hap += int(all_prize)
    if n[: 3] == f31[: 3] :
        hap += int(f31_prize)
    if n[: 3] == f32[: 3] :
        hap += int(f32_prize)
    if n[-3 :] == b31[-3 :] :
        hap += int(b31_prize)
    if n[-3 :] == b32[-3 :] :
        hap += int(b32_prize)
    if n[-2 :] == b2[-3 :] :
        hap += int(b2_prize)
    #print(all[: 3], f31[: 3], all[-3 :], b31[-3 :])
    print(hap)