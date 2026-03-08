# 29308 Закат

n = int(input())

res = 0
res_s = 0
for i in range(n) :
    s = input()
    a, b, c = s.split()
    a = int(a)
    if c == 'Russia' and a > res :
        res = a
        res_s = b
        #print(res, res_s)
print(res_s)