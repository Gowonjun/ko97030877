# 18412 文字列の反転 (Inversion of a String)

N, A, B = map(int, input().split())
S = input()
print(S[: A - 1], end = '')
print(S[A - 1 : B][::-1], end = '')
print(S[B :])