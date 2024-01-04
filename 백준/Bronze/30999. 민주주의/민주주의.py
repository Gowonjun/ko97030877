N, M = map(int, input().split())
cnt = 0
for i in range(N) :
    s = input()
    O = s.count('O')
    X = s.count('X')
    if O > X :
        cnt += 1
print(cnt)