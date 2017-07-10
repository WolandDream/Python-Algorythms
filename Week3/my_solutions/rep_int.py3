def rep_int(n):
    counter = 0
    k = n
    l = 1
    summand = []
    while k > 2*l:
        counter += 1
        summand.append(l)
        k -= l
        l += 1
    else:
        counter += 1
        summand.append(k)
    return counter, summand

def __main__():
    n = int(input())
    m, summand = rep_int(n)
    s = ''
    for i in range(len(summand)):
        s += str(summand[i]) + ' '
    print(str(m) + '\n' + s)
    
__main__()