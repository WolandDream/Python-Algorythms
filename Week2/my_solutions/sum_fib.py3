def sum_fib(n):
    div = [0,1]
    index = 0
    for i in range(1, 101):
        div.append((div[i] + div[i - 1]) % 10)
        if div[i] == div[0] and div[i+1] == div[1]:
            index = i
            break
    
    return (div[(n+2) % index] - 1) % 10

def __main__():
    n = int(input())
    print (sum_fib(n))

__main__()