def ad_place(a,b):
    value = 0
    for i in range(len(a)):
        value += a[i]*b[i]
    return value


import sys
a = []
b = []
j = 0
input = sys.stdin.read()
tokens = input.split('\n')
#print (tokens)
n = int(tokens[0].split()[0])
#print (n, W)
for line in tokens:
    if line != '' and j == 1:
        for item in line.split():
            a.append(int(item))
        j += 1
    elif  j == 2:
        for item in line.split():
            b.append(int(item))
        j += 1
    else:
        j += 1
a.sort()
b.sort()
#print (a)
#print (b)
print (ad_place(a,b))