while True :
    s = input()
    if s == '# 0 0' :
        break
    name, age, weight = s.split()
    if int(age) > 17 or int(weight) >= 80 :
        print(name, 'Senior')
    else :
        print(name, 'Junior')