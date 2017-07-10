def partial_fib_sum(n, m):
    div = [0,1]
    index = 0
    for i in range(1, 101):
        div.append((div[i] + div[i - 1]) % 10)
        if div[i] == div[0] and div[i+1] == div[1]:
            index = i
            break
    
    return (div[(n+2) % index] - div[(m+1) % index])  % 10

import sys

input = sys.stdin.read()
tokens = input.split()
m = int(tokens[0])
n = int(tokens[1])

print(partial_fib_sum(n,m))