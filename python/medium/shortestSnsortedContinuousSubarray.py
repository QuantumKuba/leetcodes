from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = -1, -2  # Initialized so that end - start + 1 = 0 for already sorted arrays
        max_seen, min_seen = nums[0], nums[-1]
        
        for i in range(n):
            max_seen = max(max_seen, nums[i])
            if nums[i] < max_seen:
                end = i
        
        for i in range(n - 1, -1, -1):
            min_seen = min(min_seen, nums[i])
            if nums[i] > min_seen:
                start = i

        return end - start + 1
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))  # Output: 5
    print(solution.findUnsortedSubarray([1, 2, 3, 4]))            # Output: 0
    print(solution.findUnsortedSubarray([1]))                     # Output: 0
    print(solution.findUnsortedSubarray([1, 3, 2, 2, 2]))        # Output: 4
