# 33689 CPDU

cnt = 0
N = int(input())
for i in range(N) :
    s = input()
    if s[0] == 'C' :
        cnt += 1
        # print(s[0], cnt)
print(cnt)