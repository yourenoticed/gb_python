while True:
    fact_request = input("Enter a number for factorial: ")
    if fact_request.isdigit():
        fact_request = int(fact_request)
        break
    
    else:
        print("Please, enter a number")

fact = 1
count = 1
while count <= fact_request:
    fact *= count
    count += 1

print(fact)
