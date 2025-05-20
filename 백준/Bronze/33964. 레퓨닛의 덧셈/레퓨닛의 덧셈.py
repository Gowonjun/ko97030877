# 33964 레퓨닛의 덧셈

def repunit(n) :
    s = '1' * n
    return int(s)

X, Y = map(int, input().split())
print(repunit(X) + repunit(Y))