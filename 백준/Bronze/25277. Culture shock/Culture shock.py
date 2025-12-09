# 25277 Culture shock

p = ['he', 'him', 'she', 'her'] # prohibit

N = int(input())
L = list(input().split())
cnt = 0
for elem in L :
    if elem in p :
        cnt += 1
print(cnt)