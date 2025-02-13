# 4880  다음수

while True :
    s = input()
    if s == '0 0 0' :
        break
    a1, a2, a3 = map(int, s.split()) 
    if a2 - a1 == a3 - a2 :
        print('AP', a3 + (a3 - a2))
    else :
        print('GP', (a3 // a2) * a3)