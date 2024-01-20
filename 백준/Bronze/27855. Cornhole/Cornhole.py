H1, B1 = map(int, input().split())
H2, B2 = map(int, input().split())
n1 = 3 * H1 + B1
n2 = 3 * H2 + B2
n = n1 - n2
if n > 0 :
    print(1, n)
elif n < 0 :
    print(2, -1 * n)
else :
    print('NO SCORE')