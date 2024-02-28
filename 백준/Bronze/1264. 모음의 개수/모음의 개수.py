v = 'AEIOUaeiou' # vowel
while True :
    cnt = 0
    s = input()
    if s == '#' :
        break
    for elem in s :
        if elem in v :
            cnt += 1
    print(cnt)