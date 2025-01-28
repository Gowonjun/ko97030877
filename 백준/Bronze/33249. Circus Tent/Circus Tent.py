# 33249 Circus Tent

from math import pi
d, h = map(float, input().split())
s = 0   # s = surface
s = pow(((d + 10) / 2), 2) * pi + (d + 10) * pi * h
print(s)