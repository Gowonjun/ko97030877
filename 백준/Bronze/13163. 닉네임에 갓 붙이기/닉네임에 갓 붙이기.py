# 13163 닉네임에 갓 붙이기

T = int(input())
for _ in range(T) :
    s = input()
    L = list(s.split())
    #print(L)
    L.pop(0)
    #print(L)
    ss = ''.join(L)
    ss = 'god' + ss
    print(ss)