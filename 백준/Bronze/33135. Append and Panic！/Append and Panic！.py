# 33135 Append and Panic!

S = input()
cnt = 0
s = set(S)
L = []
for elem in s :
    L.append(ord(elem))
L.sort()
for i in range(1, len(S)) :
    if chr(L[0]) == S[-i] :
        break
    else :
        cnt += 1
print(len(S) - cnt - 1)