# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
first_index = 0
second_index = 1

for i in range(0, n):
    if a[i] > a[first_index]:
        first_index = i

c = a[0]
a[0] = a[first_index]
a[first_index] = c

for i in range(1, n):
    if a[i] > a[second_index]:
        second_index = i

result = a[0]*a[second_index]
print(result)
