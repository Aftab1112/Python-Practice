user_string = input("Enter a string : ")

for char in user_string:
    if user_string.count(char) == 1:
        print(f"Non repeated character is {char}")
        break
