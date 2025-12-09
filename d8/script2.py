def make_union_find(n):
    parent = list(range(n))
    size = [1] * n
    return parent, size


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, size, a, b):
    ra = find(parent, a)
    rb = find(parent, b)
    if ra == rb:
        return False
    if size[ra] < size[rb]:
        parent[ra] = rb
        size[rb] += size[ra]
    else:
        parent[rb] = ra
        size[ra] += size[rb]
    return True


def distance(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2


input = open('./input.txt').read().strip().splitlines()
junctions = [tuple(map(int, row.split(','))) for row in input]
pairs = []  # dist, p, q
n = len(junctions)


for i in range(n-1):
    for j in range(i+1, n):
        pairs.append(
            (distance(junctions[i], junctions[j]), i, j))

pairs.sort()

parent, size = make_union_find(n)
conns = 0

answer = 0
for dist, i, j in pairs:
    if union(parent, size, i, j):
        answer = junctions[i][0] * junctions[j][0]

print(answer)
