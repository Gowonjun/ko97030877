# 3059  등장하지 않는 문자의 합

T = int(input())
for _ in range(T) :
    s = input()
    hap = 0
    for i in range(26) :
        #print(chr(i + 65))
        if chr(i + 65) not in s :
            hap += i + 65
            #print(hap)
    print(hap)