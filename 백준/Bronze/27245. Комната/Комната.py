w = int(input())
l = int(input())
h = int(input())
if min(w, l) >= 2 * h and max(w, l) <= 2 * min(w, l) :
    print('good')
else :
    print('bad')