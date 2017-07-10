#Uses python3

import sys

def edit_distance(s, t):
    edit_dist = []
    #print(len(t))
    for i in range(len(s) + 1):
        if i == 0:
            edit_dist.append(list(range(len(t) + 1)))
        else:
            edit_dist.append([i] + [0]*(len(t)))
    #print (edit_dist)
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            insert = edit_dist[i][j - 1] + 1
            delete = edit_dist[i - 1][j] + 1
            match = edit_dist[i - 1][j - 1]
            mismatch = edit_dist[i - 1][j - 1] + 1
            if s[i - 1] == t[j - 1]:
                #print s[i - 1]
                edit_dist[i][j] = min(insert, delete, match)
            else:
                edit_dist[i][j] = min(insert, delete, mismatch)
    return edit_dist

def backtracking(edit_dist, a):
    sub_seq = []
    i = len(edit_dist) - 1
    j = len(edit_dist[len(edit_dist) - 1]) - 1
    while i != 0 and j != 0:
        if edit_dist[i][j] == edit_dist[i - 1][j] + 1:
            i -= 1
        elif edit_dist[i][j] == edit_dist[i][j - 1] + 1:
            j -= 1
        elif edit_dist[i][j] == edit_dist[i - 1][j - 1] + 1:
            i -= 1
            j -= 1
        else:
            sub_seq.append(a[i - 1])
            i -= 1
            j -= 1
    return reversed(sub_seq)                  
def lcs3(a, b, c):
    lcs = []
    for i in range(len(a) + 1):
        lcs.append([])
        for j in range(len(b) + 1):
            lcs[i].append([0] * (len(c) + 1))
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            for k in range(len(c) + 1):
                if i == 0 or j == 0 or k == 0:
                    lcs[i][j][k] = 0
                elif a[i - 1] == b[j - 1] and b[j - 1] == c[k - 1]:
                    lcs[i][j][k] = lcs[i - 1][j - 1][k - 1] + 1
                else:
                    lcs[i][j][k] = max(lcs[i-1][j][k], lcs[i][j - 1][k], lcs[i][j][k - 1])
                   
    return lcs[len(a)][len(b)][len(c)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
