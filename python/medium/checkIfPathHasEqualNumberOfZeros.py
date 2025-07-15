from functools import cache
from typing import List


class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        @cache
        def dfs(i, j, numberOf1s):
            # if we are out of bounds - we hit a wall, cant go further
            if i >= rows or j >= columns:
                return False
            # we add the value of current cell to numberOf1s, since we can only
            # add 0 and 1 numberOf1s represents the total number of 1s encountered
            numberOf1s += grid[i][j]

            # 1) If the number of 1s we've seen so far (numberOf1s) is already more
            # than half the total steps (steps), then we know we won’t be able to
            # balance the 0s and 1s anymore.
            # 2) This means we’ve seen too many 0s. i+j+1 gives us the steps taken -numberOf1s gives
            # us the number of 0s
            if numberOf1s > steps or i + j + 1 - numberOf1s > steps:
                return False

            #If we’ve reached the bottom-right corner, we check whether the number of 1s (numberOf1s)
            # equals steps (half the total steps).

            # If yes → return True (we found a valid path).
            # If not → return False.
            if i == rows - 1 and j == columns - 1:
                return numberOf1s == steps

            #So we recursively explore both directions
            return dfs(i + 1, j, numberOf1s) or dfs(i, j + 1, numberOf1s)

        rows, columns = len(grid), len(grid[0])
        steps = rows + columns - 1 # total number of steps in a valid path


        # our condition is to have equal number of 0s and 1s in the path.
        # This is ONLY possible if we have EVEN number for the total number 
        # of steps (s)
        if steps & 1:
            return False

        # bitwise trick to devide by 2 ( it shifts the value 1 bit right
        # so if 6 is 110 in binary, it becomes 11 which is 3)
        steps >>= 1
        return dfs(0, 0, 0)