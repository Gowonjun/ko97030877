T = int(input())
for i in range(T) :
    n = int(input())
    if n > 4500 :
        a = 'Round 1'
    elif n > 1000 :
        a = 'Round 2'
    elif n > 25 :
        a = 'Round 3'
    else :
        a = 'World Finals'
    print('Case #%d: %s' % (i + 1, a))