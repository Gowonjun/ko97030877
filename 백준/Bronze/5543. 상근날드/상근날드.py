L = []
T = []
for i in range(3) :
    L.append(int(input()))
for _ in range(2) :
    T.append(int(input()))
print(min(L) + min(T) - 50)