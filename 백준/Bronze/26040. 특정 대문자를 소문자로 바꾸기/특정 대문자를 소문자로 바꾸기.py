# 26040 특정 대문자를 소문자로 바꾸기

A = list(input())
B = list(input())
for i in range(len(B)) :
    for j in range(len(A)) :
        if A[j] == B[i] :
            A[j] = chr(ord(A[j]) + 32)
print(''.join(A))