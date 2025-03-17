# 33612 피갤컵

N = int(input())
year = 2024
month = 1
month += N * 7
year += month // 12
month = month % 12
if month == 0 :
    month = 12
    year -= 1
print(year, month)