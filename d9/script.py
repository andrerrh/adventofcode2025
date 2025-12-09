input = open('./input.txt').read().strip().splitlines()
mat = [tuple(map(int, value.split(','))) for value in input]

ans = 0
for index, (x, y) in enumerate(mat):
    for nx, ny in mat[index + 1:]:
        ans = max(
            ans,
            abs(x - nx + 1) * (y - ny + 1)
        )

print(ans)
