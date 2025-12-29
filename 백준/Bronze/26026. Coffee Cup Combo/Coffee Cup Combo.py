# 26026 Coffee Cup Combo

n = int(input())
s = input()
res = 0
cnt = 0
for elem in s :
    if elem == '1' :
        cnt = 3
    if cnt > 0 :
        res += 1
    cnt -= 1
print(res)