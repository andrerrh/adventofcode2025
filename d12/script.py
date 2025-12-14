input = open('./input.txt').read().strip().split('\n\n')
temp_trees = input[6].splitlines()
trees = [tuple(map(int, tree.split(':')[0].split('x'))) for tree in temp_trees]
gifts = [sum(map(int, tree.split(':')[1].split())) for tree in temp_trees]

ans = 0
for i, (x, y) in enumerate(trees):
    print(x, y, gifts[i])
    if (x // 3) * (y // 3) >= gifts[i]:
        ans += 1

print(ans)
