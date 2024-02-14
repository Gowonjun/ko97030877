def inp() :
    a = int(input())
    return a
A1 = inp()
A2 = inp()
A3 = inp()
print(min(A2 * 2 + A3 * 4, A1 * 2 + A3 * 2, A2 * 2 + A1 * 4))