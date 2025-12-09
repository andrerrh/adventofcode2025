input = open('./input.txt').read().strip().splitlines()

ans = 0

for bank in input:
    stack = []
    for i, b in enumerate(bank):
        battery = int(b)
        while stack and stack[-1] < battery and (i != len(bank) - 1 or len(stack) == 2):
            stack.pop()

        if len(stack) < 2:
            stack.append(battery)
    else:
        ans += stack[0] * 10 + stack[1]

print(ans)
