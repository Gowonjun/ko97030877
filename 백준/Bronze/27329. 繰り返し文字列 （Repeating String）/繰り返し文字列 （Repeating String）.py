# 27329 繰り返し文字列 (Repeating String)

N = int(input())
S = input()
a = S[ : N // 2]
if a * 2 == S :
    print('Yes')
else :
    print('No')