from typing import List, Set, Tuple

# returns if the arr is equals to 1
def is_equal_to_one(arr: List[int]) -> Tuple[bool, int]:
    total = 0
    index_of_one = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            index_of_one = i
        total += arr[i]

    return [total == 1, index_of_one]


def grid_to_set(grid: List[List[int]]) -> Set[Tuple[int, int]]:
    res = set()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                res.add((i, j))
    
    return res

            


# do not modify below this line

output1 = grid_to_set([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
print(type(output1))
print(sorted(list(output1)))
      
output2 = grid_to_set([[1, 0, 0], [0, 0, 0]])
print(type(output2))
print(sorted(list(output2)))

output3 = grid_to_set([[1, 1, 1], [1, 1, 1]])
print(type(output3))
print(sorted(list(output3)))

output4 = grid_to_set([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print(type(output4))
print(sorted(list(output4)))