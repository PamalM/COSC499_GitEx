# Student Name & #: Pamal Mangat - 62994785
# Course: COSC 499 - Capstone Project; (GitHub Ex #1)


def average(list):
    total = 0
    for y in list:
        total += int(y)
    length = len(array)
    return round(total / length, 2)


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
print('\nThe array has been initialized:\n', str(array))

# View initialized array's stats.
print('\nInteger array [Max-Value]: ', max(array))
print('Integer array [Min-Value]: ', min(array))
print('Integer array [Average]: ', average(array))
