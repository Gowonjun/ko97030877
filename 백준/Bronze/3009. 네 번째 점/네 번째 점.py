X, Y = [], []
for i in range(3) :
    x, y = input().split()
    X.append(x)
    Y.append(y)
for elem in X :
    if X.count(elem) == 1 :
        x = elem
        break
for elem in Y :
    if Y.count(elem) == 1 :
        y = elem
        break
print(x, y)