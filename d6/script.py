input = open('./input.txt').read().strip().splitlines()
mat = [item.split() for item in input]

m, n = len(mat), len(mat[0])

ans = 0
for c in range(n):
    curr = int(mat[0][c])
    for r in range(1,m-1):
        value = int(mat[r][c])
        curr = curr * value if mat[-1][c] == '*' else curr + value

    ans += curr

print(ans)
