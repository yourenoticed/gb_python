#           0   1  2  3  4
# numbers = [0, -1, 5, 2, 3]
amount = int(input("Enter amount of number you want to insert: "))
numbers = list()
for _ in range(amount):
    numbers.append(int(input("Enter a number: ")))
count = 0
for i in range(1, len(numbers)):
    if numbers[i - 1] < numbers[i]:
        count += 1

print(f"{numbers}, amount of numbers: {count}")