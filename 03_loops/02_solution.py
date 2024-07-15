number = int(input("Enter a number to calculate the sum of even numbers : "))
sum_of_even = 0

for i in range(1, number +  1) : 
    if i % 2 == 0 :
        sum_of_even += i
print(f"Sum of even numbers is {sum_of_even}")