marks = int(input("Please enter your marks : "))

if marks > 100 :
    print("Please enter marks between 0 to 100")
    exit()
    
if marks >= 90 :
    grade = "A"
elif marks >= 80 :
    grade = "B"
elif marks >= 70 :
    grade = "C"
elif marks >= 60 :
    grade = "D"
else :
    grade = "F"
    
print(f"You have {marks} marks and your grade is {grade}")