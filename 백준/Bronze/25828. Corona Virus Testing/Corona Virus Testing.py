g, p, t = map(int, input().split()) # g = groups, p = people
n1 = g * p
n2 = g + t * p
if n1 < n2 :
    print(1)
elif n1 > n2 :
    print(2)
else :
    print(0)