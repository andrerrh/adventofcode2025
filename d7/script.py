input = open('./input.txt').read().strip().splitlines()
mat = [list(s) for s in input]

m, n = len(mat), len(mat[0])
start_i = mat[0].index('S')
mat[1][start_i] = '|'

ans = 0
for r in range(2, m):
    for c in range(n):
        value = mat[r][c]
        if value == '^' and mat[r-1][c] == '|':
            ans += 1
            if c > 0: mat[r][c-1] = '|'
            if c < n - 1: mat[r][c+1] = '|'
        elif value == '.' and mat[r-1][c] == '|':
            mat[r][c] = '|'

print(ans)
