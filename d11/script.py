from functools import cache

input = open('./input.txt').read().strip().splitlines()

paths = {}
for row in input:
    parent, *values = row.replace(':', '').split()
    paths[parent] = values

@cache
def dfs(node: str) -> int:
    if node == 'out':
        return 1

    acc = 0
    for nei in paths[node]:
        acc += dfs(nei)

    return acc

print(dfs('you'))
