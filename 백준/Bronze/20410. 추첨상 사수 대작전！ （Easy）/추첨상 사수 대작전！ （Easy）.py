# 20410 추첨상 사수 대작전! (Easy)

m, S, X1, X2 = map(int, input().split())
for a in range(1, m) :
    for c in range(1, m) :
        if (a * S + c) % m == X1 and (a * X1 + c) % m == X2 :
            print(a, c)
            exit()