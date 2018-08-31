import time
name = input("Please enter your name. ")
age = int(input("Please enter your age. "))
repeat = int(input("How many times should we repeat the message? "))

year_100 = 100 - age + int((time.strftime("%Y")))

for x in range(0,repeat):
    print(f"Thanks, {name}! You're currently {age} years old, and you're going to turn 100 during Year {year_100}.")