number = int(input("Enter a number to check if it is prime number or not : "))
orignal_number = number
is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % 2) == 0:
            is_prime = False
            break

print(f"{is_prime}")
