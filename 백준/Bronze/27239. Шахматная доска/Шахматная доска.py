n = int(input())
if (n - 1) // 8 == 0 :
    y = '1'
elif (n - 1) // 8 == 1 :
    y = '2'
elif (n - 1) // 8 == 2 :
    y = '3'
elif (n - 1) // 8 == 3 :
    y = '4'
elif (n - 1) // 8 == 4 :
    y = '5'
elif (n - 1) // 8 == 5 :
    y = '6'
elif (n - 1) // 8 == 6 :
    y = '7'
elif (n - 1) // 8 == 7 :
    y = '8'
if n % 8 == 1 :
    x = 'a'
elif n % 8 == 2 :
    x = 'b'
elif n % 8 == 3 :
    x = 'c'
elif n % 8 == 4 :
    x = 'd'
elif n % 8 == 5 :
    x = 'e'
elif n % 8 == 6 :
    x = 'f'
elif n % 8 == 7 :
    x = 'g'
elif n % 8 == 0 :
    x = 'h'
print(x + y)    