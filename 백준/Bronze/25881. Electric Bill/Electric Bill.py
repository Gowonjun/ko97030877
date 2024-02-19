f, ad = map(int, input().split())    # first, additional
n = int(input())
for i in range(n) :
    hap = 0
    a = int(input())   
    if a > 1000 :        
        hap += 1000 * f
        aa = a - 1000
        hap += aa * ad
    else :
        hap += a * f
    print(a, hap)