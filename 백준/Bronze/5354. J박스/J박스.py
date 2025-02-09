# 5354  J박스

T = int(input())
for _ in range(T) :
    n = int(input())
    if n == 1 :
        print('#')
    else :
        print('#' * n)
        for _ in range(n - 2) :
            print('#', end = '')
            print('J' * (n - 2), end = '')
            print('#')
        print('#' * n)
    print()