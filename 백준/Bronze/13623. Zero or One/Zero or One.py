a, b, c = map(int, input().split())
if a == b == c :
    print('*')
elif a == b :
    print('C')
elif a == c :
    print('B')
elif b == c :
    print('A')