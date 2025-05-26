# 11648 지속

cnt = 0
s = input()
while True :
    n = 1
    if len(s) == 1 :
        print(cnt)
        break    
    for elem in s :
        n *= int(elem)
    s = str(n)
    cnt += 1