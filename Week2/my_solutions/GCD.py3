def GCD(a, b):
    #print (a, b)
    if b > a:
        c = a
        a = b
        b = c
    if b != 0:
        a = a % b
        GCD(a, b)
    else:
        print(a)
    
import sys

input = sys.stdin.read()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])

GCD(a,b)