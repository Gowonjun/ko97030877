# 1110  더하기 사이클

N = int(input())
i = 0
a = N
while True :
    i += 1
    new = a // 10 + a % 10
    new = (a % 10) * 10 + new % 10
    a = new
    if a == N :
        break
print(i)