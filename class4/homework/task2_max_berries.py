# using files
""" with open(r'berries/garden1.txt', 'r') as file: # will only work if you run code in class4/homework directory
    berries_amounts = file.readline().split()

for i, val in enumerate(berries_amounts):
    if val.isdigit():
        berries_amounts[i] = int(val) """
        
# OR without using files:
berries_amounts = [1, 2, 3, 4]
max_berries = berries_amounts[0]

for i, val in enumerate(berries_amounts):
    curr_berries = berries_amounts[(i - 1)] + val + berries_amounts[(i + 1) % len(berries_amounts)]
    if curr_berries > max_berries:
        max_berries = curr_berries

print(max_berries)
