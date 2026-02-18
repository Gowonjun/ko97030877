# 5342  Billing

hap = 0
while True :
    s = input()
    if s == 'EOI' :
        break
    else :
        if s == 'Paper' :
            hap += 57.99
        elif s == 'Printer' :
            hap += 120.5
        elif s == 'Planners' :
            hap += 31.25
        elif s == 'Binders' :
            hap += 22.5
        elif s == 'Calendar' :
            hap += 10.95
        elif s == 'Notebooks' :
            hap += 11.2
        else :
            hap += 66.95
print('$%.2f' % hap)