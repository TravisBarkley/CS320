# determine if a list is made up of a repeating pattern

# import math # optional and you can delete this line if not useful

# subroutines if any, go here


# fill in repeat
def longest_path(torus):
    
    if torus is None: 
        return []
    
    if len(torus) == 0:
        return []

    if len(torus[0]) == 0: 
        return []

    m = len(torus)
    n = len(torus[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(x, y, memo):
        if (x, y) in memo:
            return memo[(x, y)]

        longest = []
        for dirX, dirY in directions:
            newX = (x + dirX) % m
            newY = (y + dirY) % n  
            if torus[newX][newY] > torus[x][y]:
                path = dfs(newX, newY, memo)
                if len(path) >= len(longest):
                    longest = path

        memo[(x, y)] = [(x, y)] + longest
        return memo[(x, y)]

    longest_path = []
    memo = {}
    for i in range(m):
        for j in range(n):
            path = dfs(i, j, memo)
            if len(path) > len(longest_path):
                longest_path = path

    return longest_path if len(longest_path) >= 2 else []


torus = [
    [1, 1, 3, 1],
    [1, 1, 1, 1],
    [1, 3, 2, 1],
    [1, 1, 1, 1]
]

print(longest_path(torus))
