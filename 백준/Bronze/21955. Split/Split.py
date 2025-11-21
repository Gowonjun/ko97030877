# 21955 Split

N = input()
n = len(N) // 2
print(N[0 : n], N[n : -1] + N[-1])