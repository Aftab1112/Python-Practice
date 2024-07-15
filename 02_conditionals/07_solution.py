coffee_size = input("Please enter the size of your coffee (small, medium, large): ").lower()
if coffee_size not in ["small", "medium", "large"]:
    print("Invalid size. Please enter small, medium, or large.")
    exit(1)

extra_shot = input("Do you want to add an extra shot of espresso? (yes or no): ").lower()
if extra_shot not in ["yes", "no"]:
    print("Invalid option. Please enter yes or no.")
    exit(1)

if extra_shot == "yes":
    extra_shot = True
else:
    extra_shot = False

if extra_shot:
    print(f"You ordered a {coffee_size} size coffee with an extra shot of espresso.")
else:
    print(f"You ordered a {coffee_size} size coffee.")
