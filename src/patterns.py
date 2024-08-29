import random

import chosen

# List to store the pattern
sequence = []
rows = 7
columns = 7


def square(uncommon, common):
    """Prints a pyramid pattern"""
    sequence.clear()

    # Randomly picks the odd one's index
    rare_index = random.choice(list(range(0, 49)))
    index = 0

    for row in range(rows):
        for column in range(columns):

            # If index = index of odd one then append the odd one
            if index == rare_index:
                sequence.append(uncommon)
                index += 1

            else:
                sequence.append(common)
                index += 1
    return rare_index

