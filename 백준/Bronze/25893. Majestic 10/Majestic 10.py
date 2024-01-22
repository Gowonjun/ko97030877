n = int(input())
for i in range(n) :
    cnt = 0
    a, b, c = map(int, input().split())
    print(a, b, c)
    if a >= 10 :
        cnt += 1
    if b >= 10 :
        cnt += 1
    if c >= 10 :
        cnt += 1
    if cnt == 0 :
        print('zilch')
    elif cnt == 1 :
        print('double')
    elif cnt == 2 :
        print('double-double')
    elif cnt == 3 :
        print('triple-double')
    print()