input = open('./input.txt').read().strip().splitlines()
mat = [tuple(map(int, value.split(','))) for value in input]


