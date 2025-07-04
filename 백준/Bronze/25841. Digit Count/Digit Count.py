# 25841 Digit Count

cnt = 0
a, b, c = map(int, input().split())
for i in range(a, b + 1) :
    #print(i)
    i = str(i)
    cnt += i.count(str(c))
print(cnt)