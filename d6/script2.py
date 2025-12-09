import math


input = open('./input.txt').read().splitlines()

mat, ops = input[:-1], input[-1]
m, n = len(mat), len(mat[0])

ans = 0
acc = []
for c in range(n-1, -1, -1):
    curr = mat[0][c]
    for r in range(1, m):
        val = mat[r][c]
        curr = curr + val
        
    if curr.strip().isnumeric():
        acc.append(int(curr))
    if ops[c] == ' ': continue
    if ops[c] == '*':
        ans += math.prod(acc)
    else:
        ans += sum(acc)
    acc = []

print(ans)

