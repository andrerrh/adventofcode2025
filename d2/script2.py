input = open('./input.txt').read().strip().split(',')

pairs = (map(int, p.split('-')) for p in input)

def is_repetition(s):
    return s in (s+s)[1:-1]

ans = 0

for start, end in pairs:
    for num in range(start, end + 1):
        if is_repetition(str(num)):
            ans += num

print(ans)
