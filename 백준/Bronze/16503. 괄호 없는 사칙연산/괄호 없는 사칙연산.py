# 16503 괄호 없는 사칙연산

s = input()
#print(s[ : 5], eval(s[ : 5]), int(eval(s[ : 5])), s[5 : ])
#first = int(eval(str(int(eval(s[ : 5]))) + s[5 : ]))
#second = int(eval(s[0 : 4] + str(int(eval(s[4 : ])))))

L = list(s.split())
first = int(eval(str(int(eval(L[0] + L[1] + L[2]))) + L[3] + L[4]))
second = int(eval(L[0] + L[1] + str(int(eval(L[2] + L[3] + L[4])))))

#print(first, second)
print(min(first, second))
print(max(first, second))