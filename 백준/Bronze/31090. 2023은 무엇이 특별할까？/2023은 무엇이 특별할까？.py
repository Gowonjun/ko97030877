T = int(input())
for i in range(T) :
    N = input()
 #   if int(N[2:3]) == 0 :
 #       continue
    if (int(N) + 1) % (int(N[2:])) == 0 :
        print('Good')
    else :
        print('Bye')