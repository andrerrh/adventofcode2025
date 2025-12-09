input = open('./input.txt').read().strip().split('\n\n')

ranges_temp, values_temp = (part.splitlines() for part in input)
ranges = [list(map(int, r.split('-'))) for r in ranges_temp]
values = [int(val) for val in values_temp]

ranges.sort(key=lambda item: (item[0], item[1]))

merged: list[list[int]] = []

for start, end in ranges:
    if not merged or start > merged[-1][1]:
        merged.append([start,end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

ans = 0
for start, end in merged:
    ans += end - start + 1

print(ans)
