T = int(input())
for i in range(T) :
    a, b, c, d, e, f, g, h = map(int, input().split())
    HP = a + e
    if HP < 1 :
        HP = 1
    MP = b + f
    if MP < 1 :
        MP = 1
    ATK = c + g
    if ATK < 0 :
        ATK = 0
    DEF = d + h
    print(HP + 5 * MP + 2 * ATK + 2 * DEF)