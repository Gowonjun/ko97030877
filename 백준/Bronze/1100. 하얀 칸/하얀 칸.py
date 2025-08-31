# 1100  하얀 칸

cnt = 0
chess = 8
for i in range(chess) :
    s = input()
    for j in range(chess) :
        if s[j] == 'F' and (i + j) % 2 == 0 :
            cnt += 1
print(cnt)