import sys
import os
# Add parent directory to path to import timer
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from timer import time_execution
from typing import List

class Solution:

    ## This solution works but it is not the most optimal one, we can use pythonic way to improve the performance.
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     answer = [0] * len(temperatures)
    #     i  =  0
    #     stack = []

    #     while (i < len(temperatures)):
    #         while (len(stack) != 0 and temperatures[stack[-1]] < temperatures[i]):
    #             answer[stack[-1]] = i - stack[-1]

    #             stack.pop()

    #         stack.append(i)
    #         i += 1
    #     return answer


    # @time_execution
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     n = len(temperatures)
    #     answer = [0] * n
    #     stack = []

    #     for i, temp in enumerate(temperatures):
    #         while stack and temperatures[stack[-1]] < temp:
    #             prev_index = stack.pop()
    #             answer[prev_index] = i - prev_index
    #         stack.append(i)
    #     return answer


    @time_execution
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        hottest = 0
        for i in range(n - 1, -1, -1):
            if temperatures[i] >= hottest:
                hottest = temperatures[i]
                continue

            j = i + 1
            while temperatures[j] <= temperatures[i]:
                j += res[j]
            res[i] = j - i

        return res



if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))