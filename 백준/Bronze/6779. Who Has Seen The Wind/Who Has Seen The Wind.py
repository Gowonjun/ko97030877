h = int(input())
M = int(input())
for t in range(1, M + 1) :
    A = (-6) * pow(t, 4) + h * pow(t, 3) + 2 * pow(t, 2) + t
    if A <= 0 :
        print('The balloon first touches ground at hour: %d' % t)
        break
else :
    print('The balloon does not touch ground in the given time.')