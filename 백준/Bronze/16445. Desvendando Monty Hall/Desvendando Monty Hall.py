# 16445 Desvendando Monty Hall

N = int(input())
cnt = 0

for i in range(N) :
    a = int(input())
    if a != 1 :
        cnt += 1
print(cnt)