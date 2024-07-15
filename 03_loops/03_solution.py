number = int(input("Enter which table you want : "))

for i in range(1, 11) :
    if i == 5 :
        continue
    print(f"{number} x {i} = {number * i}")