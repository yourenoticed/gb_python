with open(r'berries/garden1.txt', 'r') as file:
    berries_amounts = file.readline().split()

for i, val in enumerate(berries_amounts):
    if val.isdigit():
        berries_amounts[i] = int(val)

max_berries = 0 # or berries_amounts[0]

for i, val in enumerate(berries_amounts):
    curr_berries = berries_amounts[(i - 1)] + val + berries_amounts[(i + 1) % len(berries_amounts)]
    if curr_berries > max_berries:
        max_berries = curr_berries

print(max_berries)