fruit_color = input("Please enter the current color of your fruit : ")

if fruit_color.lower() == "green" :
    ripeness = "Unripe"
elif fruit_color.lower() == "yellow" :
    ripeness = "Ripe"
elif fruit_color.lower() == "brown" :
    ripeness = "Overripe"
else :
    print("Invalid fruit color")
    exit()

print(f"Your fruit is {ripeness}")