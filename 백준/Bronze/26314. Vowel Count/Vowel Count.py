# 26314 Vowel Count

v = 'aeiou'
n = int(input())
for _ in range(n) :
    s = input()
    v_cnt = 0
    c_cnt = 0
    for elem in s :
        if elem in v :
            v_cnt += 1
        else :
            c_cnt += 1
    print(s)
    if v_cnt > c_cnt :
        print(1)
    else :
        print(0)