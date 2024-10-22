cnt = 0
for i in range(9) :
    n = int(input())
    if n > cnt :
        cnt = n
        index = i + 1
print(cnt)
print(index)