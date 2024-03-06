# determine if a list is made up of a repeating pattern

import random  # optional and you can delete this line if not useful

# subroutines if any, go here

# fill in repeat


def placement(numobjects, map):

    if map is None:
        return None
    
    if numobjects < 1:
        return None
    
    available_spaces = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j]:
                available_spaces.append((i, j))

    if len(available_spaces) < numobjects:
        return None
    
    random.shuffle(available_spaces)
    return available_spaces[:numobjects]


map = (
    (True, True, True),
    (True, False, True),
    (True, True, True)
)
num_objects = 5
print(placement(num_objects, map))
