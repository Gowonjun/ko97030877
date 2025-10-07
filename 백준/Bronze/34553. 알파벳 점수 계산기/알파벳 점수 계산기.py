# 34553 알파벳 점수 계산기

cnt = 1
hap = 1
S = input()
L = list(S)
for i in range(1, len(S)) :
    if ord(S[i]) > ord(S[i - 1]) :
        cnt += 1
    else :
        cnt = 1
    #print(cnt)
    hap += cnt
print(hap)