N = int(input())
L = []
for i in range(N) :
    s = input()
    L.append(s)
y = L.index('yonsei')
k = L.index('korea')
if y < k :
    print('Yonsei Won!')
else :
    print('Yonsei Lost...')