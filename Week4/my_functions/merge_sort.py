def merge(b,c):
    inv_number = 0
    d = []
    while b != [] and c != []:
        if b[0] <= c[0]:
            d.append(b[0])
            b.remove(b[0])
        else:
            d.append(c[0])
            c.remove(c[0])
    else:
        d += b + c
    return d
        
def merge_sort(a):
    if len(a) == 1:
        return a
    mid = len(a) // 2
    b = merge_sort(a[0:mid])
    c = merge_sort(a[mid:len(a)])
    a_sorted = merge(b, c)
    #print(a_sorted)
    return a_sorted