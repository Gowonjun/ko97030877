# 10203 Count Vowels

T = int(input())
for i in range(T) :
    cnt = 0
    s = input()
    for elem in s :
        if elem in 'aeiou' :
            cnt += 1
    print('The number of vowels in %s is %d.' % (s, cnt))