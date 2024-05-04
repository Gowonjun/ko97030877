N = int(input())
for i in range(N) :
    cnt = 0
    s = input()
    for elem in s :
        if elem == 'U' :
            cnt += 1
        elif elem == 'D' :
            break
    print(cnt)