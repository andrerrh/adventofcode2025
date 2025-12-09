input = open('./input.txt').read().strip().splitlines()

ans = 0

for bank in input:
    stack = []
    for i, b in enumerate(bank):
        battery = int(b)
        while stack and stack[-1] < battery and (i != len(bank) - 1 or len(stack) == 12) and len(bank) - i  > 12 - len(stack):
            stack.pop()

        if len(stack) < 12:
            stack.append(battery)
    else:
        ans += int(''.join(str(val) for val in stack))

print(ans)
