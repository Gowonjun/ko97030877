# 5691  평균 중앙값 문제
while True :
    A, B = map(int, input().split())
    if A == 0 and B == 0 :
        break
    print(A - (B - A))