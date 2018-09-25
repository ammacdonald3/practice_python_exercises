# Using list comprehension, print even numbers from a list
collection = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([x for x in collection if x%2 == 0])
