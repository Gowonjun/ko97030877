# 1357  뒤집힌 덧셈

X, Y = input().split()
X = X[::-1]
Y = Y[::-1]
hap = int(X) + int(Y)
print(int(str(hap)[::-1]))