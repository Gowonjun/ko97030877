# 34363 Driving Dilemma

S = int(input())
D = float(input())
T = float(input())
S = S * 5280 / 3600
a = S * T
if a >= D :
    print('MADE IT')
else :
    print('FAILED TEST')