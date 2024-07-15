weather = input("Please enter the current weather condition : ")
weather = weather.lower()

if weather == "sunny" :
    activity = "go for a walk"
elif weather == "rainy" :
    activity = "read a book"
elif weather == "snowy" :
    activity = "build a snowman"
else : 
    print("Unknown weather type, please check your weather again")
    exit(1)
    
print(f"The current weather condition is {weather} therefore you should {activity}")
    
