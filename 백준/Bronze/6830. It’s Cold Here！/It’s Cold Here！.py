# 6830  It’s Cold Here!

t = 1000
s = ''
while True :
    try :
        a, b = input().split()
        b = int(b)
        if b < t :
            s = a
            t = b
    except :
        break
print(s)