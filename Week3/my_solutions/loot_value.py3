def loot_value(n, W, v, w):
    value = 0
    v_w = []
    for i in range(n):
        v_w.append(v[i] / w[i])
    while W !=0:
            if w[v_w.index(max(v_w))] > 0 and W >= w[v_w.index(max(v_w))]:
                value += v[v_w.index(max(v_w))]
                W -= w[v_w.index(max(v_w))]
                w[v_w.index(max(v_w))] = 0
                v_w[v_w.index(max(v_w))] = 0
            elif W < w[v_w.index(max(v_w))]:
                value += W*max(v_w)
                W = 0
            else:
                return value
    else:
        return value
    
import sys
v = []
w = []
j = 0
input = sys.stdin.read()
tokens = input.split('\n')
#print (tokens)
n = int(tokens[0].split()[0])
W = int(tokens[0].split()[1])
#print (n, W)
for line in tokens:
    if line != '' and j != 0:
        v.append(int(tokens[j].split()[0]))
        w.append(int(tokens[j].split()[1]))
        j += 1
    else:
        j += 1
#print (v)
#print (w)
print (round(loot_value(n, W, v, w), 4)) 