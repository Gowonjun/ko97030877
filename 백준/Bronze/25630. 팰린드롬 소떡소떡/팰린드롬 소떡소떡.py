# 25630 팰린드롬 소떡소떡

cnt = 0
N = int(input())
S = input()
for i in range(N // 2) :
    if S[i] != S[-i - 1] :
        cnt += 1
print(cnt)