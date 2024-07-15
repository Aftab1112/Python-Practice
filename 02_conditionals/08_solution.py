import pwinput

password = pwinput.pwinput(prompt="Please enter your password : ", mask='*')
password_length = len(password)

if password_length < 6 :
    strength = "Weak"
elif password_length < 10 :
    strength = "Medium"
else :
    strength = "Strong"
    
print(f"Your password strength is {strength}")
