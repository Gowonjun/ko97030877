N = int(input())
A = list(map(str, input().split()))
B = list(map(str, input().split()))
a = ''.join(A)
b = ''.join(B)
a = int(a)
b = int(b)
if a > b :
    print(b)
else :
    print(a)