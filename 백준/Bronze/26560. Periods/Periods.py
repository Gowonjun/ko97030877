n = int(input())

for i in range(n) :
    s = input()
    if s[-1] == '.' :
        print(s)
    else :
        print(s + '.')