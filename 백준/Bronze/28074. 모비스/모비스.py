s = input()
cnt = 0
if 'M' not in s :
    cnt += 1
if 'O' not in s :
    cnt += 1
if 'B' not in s :
    cnt += 1    
if 'I' not in s :
    cnt += 1
if 'S' not in s :
    cnt += 1
if cnt == 0 :
    print('YES')
else :
    print('NO')