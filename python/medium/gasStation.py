from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        return -1


if __name__ == "__main__":
    solution = Solution()
    gas = [1, 2, 3, 4, 5]
    cost = [2, 3, 4, 5, 1]
    print(solution.canCompleteCircuit(gas, cost))  # Output: 4