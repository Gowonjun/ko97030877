n, m, k, a, b, c = map(int, input().split())
J = n * a; R = m * b; S = k * c
if J == R and R == S :
    print('Joffrey Robb Stannis')
elif max(J, R, S) == J and J == R :
    print('Joffrey Robb')
elif max(J, R, S) == J and J == S :
    print('Joffrey Stannis')
elif max(J, R, S) == R and R == S :
    print('Robb Stannis')
else :
    if max(J, R, S) == J :
        print('Joffrey')
    elif max(J, R, S) == R :
        print('Robb')
    else :
        print('Stannis')