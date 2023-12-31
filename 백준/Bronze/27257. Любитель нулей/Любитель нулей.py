k = input()
n = -1
cnt = 0
n0 = k.count('0')
while True :
    if k[n] == '0' :
        n -= 1
        cnt += 1
        continue
    else :
        break
print(n0 - cnt)