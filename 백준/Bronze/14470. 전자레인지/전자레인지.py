def inp() :
    a = int(input())
    return a
A = inp()
B = inp()
C = inp()
D = inp()
E = inp()
cnt = 0
if A < 0 :
    cnt += abs(A) * C + D + B * E
else :
    cnt += (B - A) * E
print(cnt)