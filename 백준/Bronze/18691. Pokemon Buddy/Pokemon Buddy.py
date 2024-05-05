T = int(input())

for _ in range(T) :
    G = 0
    C = 0
    E = 0
    G, C, E = map(int, input().split())
    if C >= E :
        print(0)
    else :
        if G == 1 :
            print((E - C))
        elif G == 2 :
            print((E - C) * 3)
        elif G == 3 :
            print((E - C) * 5)