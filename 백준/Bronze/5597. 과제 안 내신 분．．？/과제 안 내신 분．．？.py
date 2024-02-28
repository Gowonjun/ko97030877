a = []
for i in range(28) :
    a.append(int(input()))

for j in range(30) :
    if a.count(j+1) == 0 :
        print(j+1)