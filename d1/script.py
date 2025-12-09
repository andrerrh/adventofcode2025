input = open('./input.txt').read().strip().splitlines()

pos = 50
ans = 0
for key in input:
    dir, value = key[0], int(key[1:])
    pos = (pos + (value if dir == 'R' else -value)) % 100

    if pos == 0:
        ans += 1

print(ans)
