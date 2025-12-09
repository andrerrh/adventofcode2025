input = open('./input.txt').read().strip().split(',')

pairs = (map(int, p.split('-')) for p in input)

ans = 0
for start, end in pairs:
    for num in range(start, end + 1):
        num_str = str(num)
        n = len(num_str)
        if num_str[:n//2] == num_str[n//2:]:
            ans += num

print(ans)
