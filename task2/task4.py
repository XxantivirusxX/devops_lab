from collections import defaultdict

inputs = input().split()
A = defaultdict(list)
B = defaultdict(list)
n = inputs[0]
m = inputs[1]
for ind1 in range(1, int(n)+1):
    value = input().strip()
    A[value].append(str(ind1))
for ind2 in range(1, int(m)+1):
    value = input().strip()
    B[value].append(str(ind2))
collection = list(B.keys())
collection.sort()
for each in collection:
    if each in A:
        print(' '.join(A[each]))
    else:
        print(-1)
