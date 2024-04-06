ds, ys = map(int, input().split())
dm, ym = map(int, input().split())
sun = ys - ds
moon = ym - dm
while sun != moon :
    if sun > moon :
        moon += ym
    else :
        sun += ys
print(moon)