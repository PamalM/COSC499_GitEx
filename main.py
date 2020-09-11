# Student Name & #: Pamal Mangat - 62994785
# Course: COSC 499 - Capstone Project; (GitHub Ex #1)

# Empty array to be filled after user prompt.
array = []

# Prompt user for integers to fill array.
print('\nEnter 5 integers to fill the empty array:')
element = None
# Append user integers into array.
for x in range(1, 6):
    element = str(input('Integer [{0}] = '.format(x)))
    array.append(element)

# View initialized array before stats.
print('\nThe array has been initialized:\n' + str(array))

# View initialized array's stats.
print('\nInteger array [Min-Value]:\n' + str(min(array)))
print('\nInteger array [Min-Value]:\n' + str(min(array)))
print('\nInteger array [Average]:\n' + str(sum(array) / len(array)))