# 25812 Nice Raises

cnt_1, cnt_2 = 0, 0
n, r = map(int, input().split())
for i in range(n) :
    a = int(input())
    if a + r > a * 2 :
        cnt_1 += 1
    elif a + r < a * 2 :
        cnt_2 += 1
if cnt_1 > cnt_2 :
    print(1)
elif cnt_1 < cnt_2 :
    print(2)
else :
    print(0)