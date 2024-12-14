# 2965  캥거루 세마리

A, B, C = map(int, input().split())
BA = B - A
CB = C - B
print(max(BA - 1, CB - 1))