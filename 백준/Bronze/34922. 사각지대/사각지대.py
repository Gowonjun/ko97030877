from math import pi

w, h = map(int, input().split())
r = int(input())
print(w * h - pow(r, 2) * pi * 1 / 4)