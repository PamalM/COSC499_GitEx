# Student Name & #: Pamal Mangat - 62994785
# Course: COSC 499 - Capstone Project; (GitHub Ex #1)

# Empty array to be filled after user prompt.
array = []

# Prompt user for integers to fill array.
print('\nEnter 5 integers to fill the empty array:')
element = None
# Append user integers into array.
for x in range(1, 6):
    element = int(input('Integer [{0}] = '.format(x)))
    array.append(element)

# View initialized array before sorting.
print('\nThe array has been initialized:\n' + str(array))

# View initialized array after sorting.
print('\nInteger array after sorting:\n' + str(sorted(array)))

print('hello world')
print('123')
