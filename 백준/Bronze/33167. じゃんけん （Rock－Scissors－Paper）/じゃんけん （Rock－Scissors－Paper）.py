# 33167 じゃんけん (Rock-Scissors-Paper)

N = int(input())
S = input()
T = input()
a, b = 0, 0
for i in range(N) :
    if S[i] == T[i] :
        continue
    else :
        if S[i] == 'R' and T[i] == 'P' :
            b += 1
        elif S[i] == 'S' :
            if T[i] == 'R' :
                b += 1
            else :
                a += 1
print(a, b)