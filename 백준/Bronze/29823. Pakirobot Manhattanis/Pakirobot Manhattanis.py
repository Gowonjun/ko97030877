def nat(num) :
    if num < 0 :
        num *= -1
    return num

n = int(input())
s = input()

N = s.count('N')
S = s.count('S')
W = s.count('W')
E = s.count('E')
cntN = nat(N - S)
cntW = nat(W - E)

print(cntN + cntW)