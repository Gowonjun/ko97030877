# 30454 얼룩말을 찾아라!

N, L = map(int, input().split())
LL = []
for i in range(N) :
    cnt = 0
    s = '0' + input() + '0'
    for i in range(1, L + 1):
        if s[i] == '1' :
            if s[i - 1] == '0' :
                cnt += 1
    LL.append(cnt)
print(max(LL), LL.count(max(LL)))