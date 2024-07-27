n = int(input())
L = list(map(int, input().split()))
hap = sum(L)
if hap % 3 == 0 :
    print('yes')
else :
    print('no')