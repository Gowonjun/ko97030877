# 16861 Harshad Numbers

n = int(input())
while True :
    s = str(n)
    hap = 0
    for elem in s :
        hap += int(elem)
    if n % hap == 0 :
        print(n)
        break
    else :
        n += 1