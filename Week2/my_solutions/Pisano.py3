def Pisano(n, m):
    div = [0 % m,1 % m]
    index = 0
    for i in range(1, m**2+1):
        div.append((div[i] + div[i - 1]) % m)
        if div[i] == div[0] and div[i+1] == div[1]:
            index = i
            break
    return div[n % index]

import sys

input = sys.stdin.read()
tokens = input.split()
n = int(tokens[0])
m = int(tokens[1])

print(Pisano(n,m))