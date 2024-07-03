N = int(input())
L = []
L = list(input())
while True :
    s = L.count('s')
    t = L.count('t')
    if s != t :
        del L[0]
    else :
        break
S = ''.join(L)
print(S)