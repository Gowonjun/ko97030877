ss = input()
s = ""
for elem in ss :
    if elem.islower() :
        s += elem.upper()
        
    else :
        s += elem.lower()
        
print(s)