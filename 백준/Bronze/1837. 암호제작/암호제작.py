flag = 0
import sys
T = sys.stdin.readline()
P, K = map(int, T.split())

for i in range(2, K) :
    if P % i == 0 :
        print('BAD', i)
        flag = 1
        break
if flag == 0 :
    print('GOOD')