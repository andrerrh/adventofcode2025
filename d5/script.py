input = open('./input.txt').read().strip().split('\n\n')

ranges_temp, values_temp = (part.splitlines() for part in input)
ranges = [list(map(int, r.split('-'))) for r in ranges_temp]
values = [int(val) for val in values_temp]

ranges.sort(key=lambda item: (item[0], item[1]))

def binary_search(target):
    l, r = 0, len(ranges) - 1
    while l <= r:
        m = (l + r) // 2
        m_lo, m_hi = ranges[m]

        if target >= m_lo and target <= m_hi:
            return True
        elif target >= m_lo:
            l = m + 1
        elif target <= m_hi:
            r = m - 1

    return False

ans = 0

for value in values:
    if binary_search(value):
        ans += 1

print(ans)
