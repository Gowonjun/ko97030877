T = int(input())
for j in range(T) :
    r, S = input().split()
    R = int(r)
    for elem in S :
        print(elem * R, end = '')
    print()