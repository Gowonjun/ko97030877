# 34722 출제자가 몇 명

N = int(input())
hap = 0
for i in range(N) :
    s, c, a, r = map(int, input().split())
    if s >= 1000 or c >= 1600 or a >= 1500 or (r > 0 and r <= 30) :
        hap += 1
print(hap)