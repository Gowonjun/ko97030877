L = ['Never gonna give you up', 'Never gonna let you down', 'Never gonna run around and desert you', 'Never gonna make you cry', 'Never gonna say goodbye', 'Never gonna tell a lie and hurt you', 'Never gonna stop']
flag = 0

N = int(input())
for i in range(N) :
    Si = input()
    if Si not in L :
        flag = 1
        break
if flag == 0 :
    print('No')
else :
    print('Yes')