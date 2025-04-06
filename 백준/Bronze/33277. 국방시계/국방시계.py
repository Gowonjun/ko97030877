# 33277 국방시계

N, M = map(int, input().split())
t = M / N * 24 * 60
print('%02d:%02d' % (t // 60, int(t % 60)))