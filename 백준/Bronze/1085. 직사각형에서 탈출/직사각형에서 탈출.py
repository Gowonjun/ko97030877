x, y, w, h = map(int, input().split())
y1 = h - y
x1 = w - x
print(min(x, y, x1, y1))