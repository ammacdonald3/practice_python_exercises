# Import sys
import sys

# Ask user to input a string
print("Let's check to see if you know what a palindome is!")
user_string = input("Please input a word or phrase: ")

# Confirm that user input a string and return an error if it's a different data type
# NOTE: Code should be updated to change string to all upper/lower to make it case-insensitive
try:
    user_string = str(user_string)
except ValueError:
    "You input an invalid value. Try following instructions next time..."
    sys.exit()


# Create a new variable that is the reverse of user input
reverse_string = user_string[::-1]


# Check if the new variable equals the user input
if reverse_string == user_string:
    print("You entered a palindrome!")
# Return confirmation/denial message
else:
    print("You did not enter a palindrome.")
        