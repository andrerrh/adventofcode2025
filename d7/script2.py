from functools import cache


input = open('./input.txt').read().strip().splitlines()
mat = [list(s) for s in input]

m, n = len(mat), len(mat[0])
start_i = mat[0].index('S')
mat[1][start_i] = '|'

def is_valid(c: int):
    if c < 0 or c == n: return False
    return True

@cache
def dfs(r: int, c: int) -> int: 
    if not is_valid(c):
        return 0
    if r == m - 1:
        return 1 
    curr = mat[r][c]
    mat[r][c] = '|'
    acc = 0
    if mat[r+1][c] == '^':
        acc += dfs(r + 1, c - 1)
        acc += dfs(r + 1, c + 1)
    if mat[r+1][c] == '.':
        acc += dfs(r + 1, c)
    mat[r][c] = curr
    return acc

ans = dfs(1, start_i)

print(ans)
