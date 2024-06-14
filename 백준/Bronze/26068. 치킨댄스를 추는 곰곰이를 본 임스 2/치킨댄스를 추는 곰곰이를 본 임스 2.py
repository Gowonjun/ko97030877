cnt = 0
N = int(input())
for i in range(N) :
    s = input()
    s = s[2:]
    s = int(s)
    if s <= 90 :
        cnt += 1
print(cnt)