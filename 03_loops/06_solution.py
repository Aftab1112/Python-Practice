number = int(input("Enter a number to calculate it's factorial : "))
orignal_number = number
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print(f"Factorial of {orignal_number} is {factorial}")
