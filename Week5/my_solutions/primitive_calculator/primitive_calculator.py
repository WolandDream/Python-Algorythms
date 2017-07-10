# Uses python3
import sys

def optimal_sequence(n):
    opt_ope = [0, ]
    sequence = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 2 == 0 :
            opt_ope.append(min(opt_ope[i // 3] + 1, opt_ope[i // 2] + 1, opt_ope[i - 1] + 1)) 
        elif i % 2 == 0:
            opt_ope.append(min(opt_ope[i // 2] + 1, opt_ope[i - 1] + 1))
        elif i % 3 == 0:
            opt_ope.append(min(opt_ope[i // 3] + 1, opt_ope[i - 1] + 1))
        else:
            opt_ope.append(opt_ope[i - 1] + 1)
    #print(opt_ope)
    i = len(opt_ope) - 1
    #print (i)
    
    while i != 0:
        #print(i)
        if i % 3 == 0 and opt_ope[i] == opt_ope[i // 3] + 1:
            sequence.append(i)
            i = i // 3
        elif i % 2 == 0 and opt_ope[i] == opt_ope[i // 2] + 1:
            sequence.append(i)
            i = i // 2
        elif opt_ope[i] == opt_ope[i - 1] + 1:
            sequence.append(i)
            i -= 1
      
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
