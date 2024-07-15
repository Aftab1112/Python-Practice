# With user input no need to pass argument


def square_of_number():
    number = int(input("Enter a number to find it's square : "))
    squared_number = number**2
    print(f"Square of {number} is {squared_number}")


square_of_number()


# Without user input it is compulsory to pass argument


def square_of_number(number):
    return number**2


result = square_of_number(10)
print(result)
