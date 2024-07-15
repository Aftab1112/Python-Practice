while True:
    number = int(input("Enter a number between 1 and 10 : "))
    if number in range(1, 11):
        print("Validation complete")
        break
    else:
        print("Invalid number, try again...")
