pet = input("Enter your pet : ")
pet.lower()
pet_age = int(input("Enter the age of your pet : "))

if pet == "dog":
    if pet_age < 2:
        print("Give your pet puppy food!")
    else:
        print("Give your pet adult dog food!")
elif pet == "cat":
    if pet_age < 5:
        print("Give your pet junior cat food!")
    else:
        print("Give your pet senior cat food!")
else:
    print("Unknown pet type. Please enter 'dog' or 'cat'.")
