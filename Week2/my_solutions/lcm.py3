def GCD(a, b):
    c = max(a,b)
    d = min(a,b)
    while True:
        if d != 0:
            sw = c
            c = d
            d = sw % d
        else:
            return c
            break
            
def lcm(a,b):
    return a*b // GCD(a,b)

import sys

input = sys.stdin.read()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])

result = lcm(a,b)
print(result)