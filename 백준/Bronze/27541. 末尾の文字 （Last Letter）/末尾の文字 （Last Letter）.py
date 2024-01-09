N = int(input())
S = input()
if S[-1] == 'G' :
    print(S[0 : -1])
elif S[-1] != 'G' :
    print(S + 'G')