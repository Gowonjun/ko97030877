w, h = map(int, input().split())
res = w + h - pow((pow(h, 2) + pow(w, 2)), 0.5)
print(res)