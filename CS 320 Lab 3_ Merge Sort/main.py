import math  # optional and you can delete this line if not useful


# subroutines if any, go here
def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# fill in mergesort
def mergesort(mlist):

    # base cases 
    if mlist is None:
        return None
    
    if len(mlist) == 0: 
        return []
    
    if len(mlist) == 1:
        return mlist
    
    # split list in half 
    midPoint = len(mlist) // 2
    left = mlist[:midPoint]
    right = mlist[midPoint:]

    # split list until they are length 1 
    left = mergesort(left)
    right = mergesort(right)

    # merge all the halves 
    return merge(left, right)


unsorted_list = [18, 9, 8, 4, 1]
sorted_list = mergesort(unsorted_list)
print(sorted_list)
