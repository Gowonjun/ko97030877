# 26004 HI-ARC

N = int(input())
S = input()
H = S.count('H')
I = S.count('I')
R = S.count('R')
A = S.count('A')
C = S.count('C')
print(min(H, I, R, A, C))