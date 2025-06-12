# 24768 Left Beehind

while True :
    s = input()
    if s == '0 0' :
        break
    x, y = map(int, s.split())
    if x + y == 13 :
        print('Never speak again.')
    else :
        if x > y :
            print('To the convention.')
        elif x < y :
            print('Left beehind.')
        else :
            print('Undecided.')