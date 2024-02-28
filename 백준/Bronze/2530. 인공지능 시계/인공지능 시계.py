A, B, C = map(int, input().split())
D = int(input())
m = D // 60
s = D % 60
C += s
while True :
    if C >= 60 :
        m += 1
        C -= 60
    else :
        break
B += m
while True :
    if B >= 60 :
        A += 1
        B -= 60
    else :
        break
while True :
    if A >= 24 :
        A -= 24
    else :
        break
print(A, B, C)