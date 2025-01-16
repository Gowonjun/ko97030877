# 33162 散歩 (Walking)

cnt = 0
x = int(input())
for i in range(x) :
    if i % 2 == 0 :
        cnt += 3
    else :
        cnt -= 2
print(cnt)