file = open("youtube.txt", "w")

try:
    file.write("Hello first method !")
finally:
    file.close()

with open("youtube.txt", "w") as file:
    file.write("Hello second method !")
