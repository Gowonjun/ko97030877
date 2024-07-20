score = []
N = int(input())
for i in range(N) :
    L = list(map(int, input().split()))
    Lr = L[: 2]
    Lr.sort(reverse = True)
    Lt = L[2 :]
    Lt.sort(reverse = True)
    hap = Lr[0] + Lt[0] + Lt[1]
    score.append(hap)
print(max(score))