s = input()
s = s[0:5]
cnt = 0

N = int(input())
for i in range(N) :
    ss = input()
    if ss[0:5] == s :
        cnt += 1
print(cnt)