a, b = map(int, input().split())
area = a * b
bag = 5 * 4840
cnt = 1
while True :
    if cnt * bag >= area :
        print(cnt)
        break
    cnt += 1