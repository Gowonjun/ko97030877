# 1297  TV 크기

# 백업

D, H, W = map(int, input().split())

s = D / (H ** 2 + W ** 2) ** 0.5

print(int(H * s), int(W * s))