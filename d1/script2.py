input = open('./input.txt').read().strip().splitlines()

pos = 50
ans = 0
for key in input:
    dir, value = key[0], int(key[1:])

    for _ in range(value):
        pos += 1 if dir == 'R' else -1
        if pos == 100: pos = 0
        if pos == -1: pos = 99
        if pos == 0: ans += 1

print(ans)
