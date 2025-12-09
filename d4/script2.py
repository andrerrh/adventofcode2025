input = open('./input.txt').read().strip().splitlines()

m, n = len(input), len(input[0])

grid = [[c for c in row] for row in input]
def check_neighbors(r, c):
    acc = 0
    for nr, nc in [[r-1, c], [r-1, c+1], [r, c+1], [r+1, c+1], [r+1, c], [r+1, c-1], [r, c-1], [r-1, c-1]]:
        if(nr < 0 or nc < 0 or nr >= m or nc >= n): continue
        if(grid[nr][nc] == '@'):
            acc += 1
    return acc < 4

ans = 0

def solve():
    global ans
    prev_ans = ans
    for r in range(m):
        for c in range(n):
            if grid[r][c] == '@'and check_neighbors(r, c):
                ans += 1
                grid[r][c] = '.'
    if prev_ans < ans:
        solve()

solve()
print(ans)
