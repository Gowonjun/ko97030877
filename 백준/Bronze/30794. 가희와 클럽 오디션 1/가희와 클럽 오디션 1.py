lv ,g = input().split() # g = grade(판정)
lv = int(lv)
if g == 'miss' :
    g = 0
elif g == 'bad' :
    g = 200
elif g == 'cool' :
    g = 400
elif g == 'great' :
    g = 600
elif g == 'perfect' :
    g = 1000
print(g * lv)