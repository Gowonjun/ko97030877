# 8371  Dyslexia

cnt = 0
n = int(input())
A = input()
B = input()
for i in range(n) :
    if A[i] != B[i] :
        cnt += 1
print(cnt)