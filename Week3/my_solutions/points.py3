def cont_points(a,b,n):
    points = []
    m = 0
    if min(b) == max(b):
        return 1, [max(b)]
    while max(a) != 0:
        point = min(b)
        m += 1
        points.append(point)
        for i in range(len(a)):
            if a[i] <= point:
                b[i] = max(b)
                a[i] = 0
    else:
        return m, points

import sys
a = []
b = []
j = 0
input = sys.stdin.read()
tokens = input.split('\n')
#print (tokens)
n = int(tokens[0])
#print (n, W)
for line in tokens:
    if line != '' and j != 0:
        a.append(int(tokens[j].split()[0]))
        b.append(int(tokens[j].split()[1]))
        j += 1
    else:
        j += 1

#print (a)
#print (b)
m, points = cont_points(a,b, n)
s = ''
for i in range(len(points)):
    s += str(points[i]) + ' '
print(str(m) + '\n' + s)
            