import sys
import os
# Add parent directory to path to import timer
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from timer import time_execution
from typing import List


class Solution:
    @time_execution
    def largestRectangleArea(self, heights: List[int]) -> int:
        # brute force: start from every column, regard it as the lowest, search left and right until meet the first lower one, so that we can calculate by that boundary. O(n^2)
        # optimize by double pointer: record the previous or latter columns' condition, so that they can be reused. O(n)
        # Monotonic Stack
        # The key point is to find the first shorter col in left and right.
        # To achieve this, stack top->bottom should be decreasing, then after meet the first col outside the stack(a) that is shorter than top, pop the top(b),new top is (c). Then b's left and right short col is a and c

        # To avoid the whole array is increasing so that no results can be stored, add 0 at both sides of the original heights
        heights.insert(0,0) #left
        heights.append(0) # right
        # start traverse 
        stack = []
        stack.append(0)
        res = 0
        hl = len(heights)
        for i in range(1,hl):
            if heights[i] > heights[stack[-1]]:
                stack.append(i)
            elif heights[i] == heights[stack[-1]]:
                stack[-1] = i
            else:
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack[-1]]
                    stack.pop()
                    w = i-stack[-1]-1
                    res = max(res,h*w)
                stack.append(i)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))