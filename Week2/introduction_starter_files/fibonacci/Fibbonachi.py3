
def FibNum(n):
    F = [0,1]    
    for i in range(1, n):
        F.append(F[i] + F[i - 1])
    
    return F[n]

def __main__():
    n = int(input())
    print (FibNum(n))

__main__()