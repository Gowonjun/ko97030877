# 10205 헤라클레스와 히드라

K = int(input())
for i in range(K) :
    h = int(input())
    s = input()
    c = s.count('c')
    b = s.count('b')
    print('Data Set %d:' % (i + 1))
    print(h + c - b)
    print()