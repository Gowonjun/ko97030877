# 28636 Марафонец

t = 0
n = int(input())
for i in range(n) :
    m, s = map(int, input().split(':'))
    t += m * 60 + s
h = t // (60 * 60)
m = (t - h * 60 * 60) // 60
s = (t - h * 60 * 60) % 60
print('%02d:%02d:%02d' % (h, m, s))