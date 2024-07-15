try:
    transport_distance = int(input("Please enter your travel distance in km : "))
except ValueError:
    print("Invalid distance, please enter a valid distance in km")
    exit(1)

if transport_distance <= 3:
    transport_mode = "walk"
elif transport_distance <= 15:
    transport_mode = "use a bike"
else:
    transport_mode = "use a car"

print(f"The transport distance is {transport_distance} km, therefore you should {transport_mode}")