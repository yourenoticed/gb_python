arr = [3, 4, 5, 14, 2, 4, 0, 3, 2, 5, 6]
""" result = list()
for i in range(len(arr)):
    if arr[i] != 0:
        result.append(arr[i])
    else:
        break
print(max(result)) """

n = int(input("Enter a number: "))
max_number = n
while n > 0:
    n = int(input("Enter a number: "))
    if max_number < n:
        max_number = n
print(max_number) 
