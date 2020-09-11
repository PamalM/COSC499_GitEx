# Student Name & #: Pamal Mangat - 62994785
# Course: COSC 499 - Capstone Project; (GitHub Ex #1)

# Empty array to be filled after user prompt.
array = []

# Prompt user for integers to fill array.
print('\nEnter 5 strings to fill the empty array:')
element = None
# Append user integers into array.
for x in range(1, 6):
    element = str(input('String [{0}] = '.format(x)))
    array.append(element)

# View initialized array before sorting.
print('\nThe array has been initialized:\n', str(array))

# View initialized array after sorting.
print('\nString array after sorting:\n', str(sorted(array)))

