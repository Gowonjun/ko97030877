# 2052  지수연산

N = int(input())
res = 1 / pow(2, N)
res = str('%.300f' % res)
#res = '111000' # test

for i in range(1, len(res) + 1) :
    if res[(-1)] == '0' :
        res = res[: -1]
        #print(res)
    else :
        break
print(res)