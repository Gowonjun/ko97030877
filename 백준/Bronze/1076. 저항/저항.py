# 1076  저항
# 백업

res = ''
L = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
for i in range(3) :
    s = input()
    a = L.index(s)
    if i < 2 :
        res += str(a)
    else :
        res = int(res) * pow(10, a)
    #print(res)
print(res)