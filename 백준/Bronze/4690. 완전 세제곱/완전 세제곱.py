for a in range(2, 101) :
    for d in range(2, a) :
        for c in range(d + 1, a) :
            for b in range(c + 1, a) :
                if a ** 3 == b ** 3 + c ** 3 + d ** 3 :
                    print("Cube = %d, Triple = (%d,%d,%d)" % (a, d, c, b))