print("Let's determine whether a number is odd or even.")
num = input("What number would you like to check? ")
divisor = input("What number should we divide it by? ")


try:
    num = int(num)
    divisor = int(divisor)
except ValueError:
    print("You didn't enter a valid number...")

if num == 0 or divisor == 0:
    print("You entered zero. We can't divide that!")
elif num % divisor == 0:
    print(f"{num} is divisible by {divisor}!")
else:
    print(f"{num} is NOT divisible by {divisor}!")