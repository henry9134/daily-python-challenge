number = int(input("Enter a number: "))

if number % 4 == 0:
    print(f"The number {number} is a multiple of 4.")
elif number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

num = int(input("Enter a number to check: "))
check = int(input("Enter a number to divide by: "))

if num % check == 0:
    print(f"{check} divides evenly into {num}.")
else:
    print(f"{check} does not divide evenly into {num}.")
