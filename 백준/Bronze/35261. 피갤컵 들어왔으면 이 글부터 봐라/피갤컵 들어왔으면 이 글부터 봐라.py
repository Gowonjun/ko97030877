# 35261 피갤컵 들어왔으면 이 글부터 봐라

n = int(input())
s = input()
target = "eagle"
min_changes = 5 

for i in range(len(s) - 4):
    current_changes = 0
    
    for j in range(5):
        if s[i + j] != target[j]:
            current_changes += 1
            
    if current_changes < min_changes:
        min_changes = current_changes

print(min_changes)