L, P = map(int, input().split())
N = L * P
List = list(map(int, input().split()))
for elem in List :
    print(elem - N)