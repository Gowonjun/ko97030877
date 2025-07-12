# 2864  5와 6의 차이

a, b = input().split()
a = a.replace('6', '5')
b = b.replace('6', '5')
minimum = int(a) + int(b)
#print(a, b)
a = a.replace('5', '6')
b = b.replace('5', '6')
maximum = int(a) + int(b)
#print(a, b)
print(minimum, maximum)