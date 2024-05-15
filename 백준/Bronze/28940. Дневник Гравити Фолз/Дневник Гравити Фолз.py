w, h = map(int, input().split())
n, a, b = map(int, input().split())
if w < a or h < b :
    print(-1)
else :
    x = 0
    x = n // (int(w / a) * int(h / b))
    if  n % (int(w / a) * int(h / b)) == 0 :
        print(x)
    else :
        print(int(x) + 1)