N = int(input())
n = N % 14 - 1
if n == - 1 :
    n += 14
s = 'WelcomeToSMUPC'
print(s[n])