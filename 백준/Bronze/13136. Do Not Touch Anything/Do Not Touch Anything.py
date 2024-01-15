R, C, N = map(int, input().split())
if R % N == 0:
    r = R // N
else :
    r = R // N + 1
if C % N == 0 :
    c = C // N
else :
    c = C // N + 1
print(r * c)