# 10833 사과

N = int(input())
hap = 0
for i in range(N) :
    a, b = map(int, input().split())
    hap += b % a
print(hap)