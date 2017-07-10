# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_and_max(i, j, m, M, op_symb):
    m_in = float('inf')
    m_ax = -float('inf')
    for k in range(i, j):
        a = evalt(M[i][k], M[k + 1][j], op_symb[k])
        b = evalt(M[i][k], m[k + 1][j], op_symb[k])
        c = evalt(m[i][k], M[k + 1][j], op_symb[k])
        d = evalt(m[i][k], m[k + 1][j], op_symb[k])
        #print(a,b,c,d)
        m_in = min(m_in, a, b, c, d)
        m_ax = max(m_ax, a, b, c, d)
    return m_in, m_ax

def get_maximum_value(dataset):
    int_symb = []
    op_symb = []
    M = []
    m = []
    for i in range(len(dataset)):
        if dataset[i] == '*' or dataset[i] == '+' or dataset[i] == '-':
            op_symb.append(dataset[i])
        else:
            int_symb.append(int(dataset[i]))
    #print (int_symb)
    #print (op_symb)
    for i in range(len(int_symb)):
        M.append([0] * len(int_symb))
        m.append([0] * len(int_symb))
        m[i][i] = int_symb[i]
        M[i][i] = int_symb[i]
    #print(M)
    for s in range(1, len(int_symb)):
        for i in range(len(int_symb) - s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(i,j, m, M, op_symb)
    return M[0][len(int_symb) - 1] 


if __name__ == "__main__":
    print(get_maximum_value(input()))
