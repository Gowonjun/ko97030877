for i in range(3) :
    Agh, Agm, Ags, Alh, Alm, Als = map(int, input().split())
    total = 3600 * (Alh - Agh) + 60 * (Alm - Agm) + (Als - Ags)
    h = total // 3600
    m = (total % 3600) // 60
    s = ((total % 3600) % 60)
    print(h, m, s)