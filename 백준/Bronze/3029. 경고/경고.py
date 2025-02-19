# 3029  경고

h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

now = h1 * 3600 + m1 * 60 + s1
throw = h2 * 3600 + m2 * 60 + s2
if now >= throw :
    throw += 24 * 3600
wait = throw - now
h3 = wait // 3600
wait -= h3 * 3600
m3 = wait // 60
s3 = wait % 60
print('%02d:%02d:%02d' % (h3, m3, s3))