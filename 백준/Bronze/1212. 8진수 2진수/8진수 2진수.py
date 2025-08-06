# 1212  8진수 2진수

n = int(input())
s = str(n)
s = '0o' + s
o = int(s, 8)
print(str(bin(o))[2 :])