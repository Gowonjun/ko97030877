N = int(input())
S = input()
cnt = 0
for elem in S :
    if elem == 'j' :
        cnt += 2
    elif elem == 'o' :
        cnt += 1
    else :
        cnt += 2
print(cnt)