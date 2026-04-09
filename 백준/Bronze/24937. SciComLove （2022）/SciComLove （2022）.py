# 24937 SciComLove (2022)

s = 'SciComLove'
n = len(s)
N = int(input())
N = N % n
for _ in range(N) :
    a = s[0]
    s = s[1 : ]
    #print(s)
    s = s + a
print(s)