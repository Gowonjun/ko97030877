# 26906 Vikingahackare

import sys
input = sys.stdin.readline

T = int(input())
code_map = {}

for _ in range(T):
    char, binary = input().split()
    code_map[binary] = char

encoded_string = input().strip()
result = ""

for i in range(0, len(encoded_string), 4):
    chunk = encoded_string[i : i+4]
    
    if chunk in code_map:
        result += code_map[chunk]
    else:
        result += "?"

print(result)