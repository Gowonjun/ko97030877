# 9783  Easy Encryption

s = input()
for elem in s :
    if elem.isalpha() == True :
        if elem.islower() == True :
            a = ord(elem) - 96
            if a < 10 :
                print('0' + str(a), end = '')
            else :
                print(a, end = '')
        else :
            a = ord(elem) - 38
            if a < 10 :
                print('0' + str(a), end = '')
            else :
                print(a, end = '')
    elif elem.isdigit() :
        print('#' + str(elem), end = '')
    else :
        print(elem, end = '')