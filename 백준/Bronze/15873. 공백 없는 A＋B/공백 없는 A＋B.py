s = input()
if s[1] == '0' :
    if len(s) == 4 :
        print(int(s[0]) * 10 + int(s[2]) * 10)
    else :
        print(int(s[0]) * 10 + int(s[2]))
else :
    if len(s) == 3 :
        print(int(s[0]) + int(s[1]) * 10)
    else :
        print(int(s[0]) + int(s[1]))