def find_lo(list, target):
    low = 0
    high = len(list)
    while low < high:
        mid = low + (high - low) // 2
        if list[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


def find_hi(list, target):
    low = 0
    high = len(list)
    while low < high:
        mid = low + (high - low) // 2
        if list[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low


def extract(list, lo, hi):

    if list is None: 
        return None
    
    if lo is None: 
        lo = float('-inf')

    if hi is None: 
        hi = float('inf')

    if hi is None and lo is None:
        return list

    if lo > hi:
        return None

    if len(list) == 0: 
        return list
    
    left = find_lo(list, lo)
    right = find_hi(list, hi)

    return list[left:right]


print(extract([-24, 3, 3, 3, 4, 5, 6, 8, 9, 10], None, None))
