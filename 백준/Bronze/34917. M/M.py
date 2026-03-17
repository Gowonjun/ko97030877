# 34917 M

def print_m_shape(m):
    mid = m // 2
    
    for r in range(m):
        row = ""
        for c in range(m):
            if c == 0 or c == m - 1 or (r <= mid and (c == r or c == m - 1 - r)):
                row += "#"
            else:
                row += "."
        print(row)

T = int(input())
for _ in range(T) :
    N = int(input())
    print_m_shape(N)