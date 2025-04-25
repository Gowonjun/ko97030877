# 21875 Innohorse
# 백업

l1 = list(input())
l2 = list(input())
#print(l1, l2)
l1[1] = int(l1[1])
l2[1] = int(l2[1])
#print(l1, l2)
print(min(abs(ord(l1[0]) - ord(l2[0])), abs(l1[1] - l2[1])), max(abs(ord(l1[0]) - ord(l2[0])), abs(l1[1] - l2[1])))