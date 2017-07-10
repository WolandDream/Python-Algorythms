def grater_or_equal(digit, max_digit):
    if int((str(digit) + str(max_digit))) >= int((str(max_digit) + str(digit))):
        return True
    else:
        return False

def large_number(a):
    number = ''
    while a != []:
        max_digit = 0
        for digit in a:
            if grater_or_equal(digit, max_digit):
                max_digit = digit
        number += str(max_digit)
        a.remove(max_digit)
    else:
        return int(number)
    

import sys
a = []
j = 0
input = sys.stdin.read()
tokens = input.split('\n')
#print (tokens)
n = int(tokens[0].split()[0])
#print (n, W)
for line in tokens:
    if j == 1:
        for item in line.split():
            a.append(int(item))
    j += 1

print (large_number(a))