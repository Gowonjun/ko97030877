# 13073 Sums

t = int(input())
for i in range(t) :
    N = int(input())
    if N % 2 == 0 :
        N_odd = N
        N_even = N + 1
        S1 = N // 2 * (1 + N)
        S2 = N // 2 * (1 + N_odd * 2 - 1)
        S3 = N // 2 * (2 + N_even* 2 - 2)
    else :
        N_even = N + 1
        N_odd = N
        S1 = N * (1 + N) // 2
        S2 = N * (1 + N_odd * 2 - 1) // 2
        S3 = N * (2 + N_even * 2 - 2) // 2
    print(S1, S2, S3)