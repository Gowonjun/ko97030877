# 14579 덧셈과 곱셈

def ar(n) :
    hap = 0
    for i in range(1, n + 1) :
        hap += i
    return hap
a, b = map(int, input().split())
res = 1
for j in range(a, b + 1) :
    res *= ar(j)
print(res % 14579)