# 14782 Bedtime Reading, I

l = int(input())
L = []
for i in range(1, l + 1) :
    if l % i == 0 :
        L.append(i)
print(sum(L))