# Uses python3
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
    return edit_dist[len(s)][len(t)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
