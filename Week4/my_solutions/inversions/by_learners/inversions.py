# Uses python3
import sys

def inv_merge(c, d):
    number_of_inversions = 0
    while c != [] and d != []:
        c1 = c[0]
        d1 = d[0]
        if c1 <= d1:
            b.append(c1)
            c.remove(c1)
        else:
            b.append(d1)
            number_ofinversions += 1
            d.remove(d1)
    else:
         b += c + d
    return b, number_of_inversions

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    b, number_of_inversions = inv_merge(a[left:ave], a[ave, right])
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
