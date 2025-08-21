# 8949  대충 더해

A, B = input().split()
s = ''
for i in range(1, max(len(A), len(B)) + 1) :
    try :
        s = str(int(A[(-1) * i]) + int(B[(-1) * i])) + s
    except :
        if len(A) > len(B) :
            s = str(int(A[(-1) * i])) + s
        else :
            s = str(int(B[(-1) * i])) + s
print(s)