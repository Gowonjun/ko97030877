P = int(input())
C = int(input())

total = 0
total += P * 50
total -= C * 10
if P > C :
    total += 500
print(total)