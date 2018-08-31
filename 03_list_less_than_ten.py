# a = [int(x) in input().split()]

s = input("Please input ten numbers separated by spaces: ")
numbers = list(map(int, s.split()))

if len(numbers) < 10:
    print("You entered less than ten numbers. Try again.")
elif len(numbers) > 10:
    print("You entered more than ten numbers. Try again.")
else:
    print("Of your input, the following numbers are less than five:")
    print([x for x in numbers if x < 5])