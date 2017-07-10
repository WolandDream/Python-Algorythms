def mon_charge(n):
    return (n // 10) + (n % 10 // 5) + (n % 10 % 5)

def __main__():
    n = int(input())
    print (mon_charge(n))

__main__()