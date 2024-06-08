L = []
N = int(input())
L = list(map(int, input().split()))
hap = sum(L)
hap = (len(L) - 1) * 8 + hap
print(hap // 24, hap % 24)
