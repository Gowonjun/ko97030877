a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())
if T < 30 :
    A = a
    B = b
elif 30 <= T and T < 45 :
    A = a + (T - 30) * 21 * x
    B = b
else :
    A = a + (T - 30) * 21 * x
    B = b + (T - 45) * 21 * y
print(A, B)