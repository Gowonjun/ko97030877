T = int(input())
N = int(input())
L = list(map(int, input().split()))
hap = sum(L)
if hap >= T :
    print('Padaeng_i Happy')
else :
    print('Padaeng_i Cry')