A, P = map(int, input().split())
n = A * 7 - P * 13
if n > 0 :
    print('Axel')
elif n < 0 :
    print('Petra')
else :
    print('lika')