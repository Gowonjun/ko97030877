# 18005 Even or Odd?

n = int(input())
a = n + n * (n + 1) // 2
n += 1
b = n + n * (n + 1) // 2
if a % 2 == 0 and b % 2 == 0 :
    print(2)
elif a % 2 == 1 and b % 2 == 1 :
    print(1)
else :
    print(0)