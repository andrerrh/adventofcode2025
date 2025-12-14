from functools import cache

input = open('./input.txt').read().strip().splitlines()

paths = {}
for row in input:
    parent, *values = row.replace(':', '').split()
    paths[parent] = values

@cache
def dfs(node: str, fft: bool, dac: bool) -> int:
    if node == 'out' and fft and dac:
        return 1
    elif node == 'out' and not (fft and dac):
        return 0

    acc = 0
    for nei in paths[node]:
        nfft, ndac = fft, dac
        if nei == 'fft': nfft = True
        if nei == 'dac': ndac = True
        acc += dfs(nei, nfft, ndac)

    return acc

print(dfs('svr', False, False))
