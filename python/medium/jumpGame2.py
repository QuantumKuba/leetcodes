from collections import deque
from typing import List


class Solution:

    # O(N^2) solution  this is because there are two nested loops
    def jump_unopt(self, nums: List[int]) -> int:
        jumps =  0
        visited = set([0])
        queue = deque([0])
        n = len(nums)

        if n == 1:
            return 0

        while queue:
            size = len(queue)

            # for each element in the current level
            for _ in range(size):
                x = queue.popleft() # with this we get the index
                visited.add(x) # add the visited index

                value = nums[x]
                
                for i in range(x + 1, min(n, x + nums[x] + 1)):
                    if i == n - 1:
                        return jumps + 1

                    if i not in visited:
                        visited.add(i)
                        queue.append(i)

            jumps += 1

            
        return jumps

    # O(N) solution 
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_jump = nums[0] # the farthest index we can reach so far. start with nums[0] because that's our first jump capacity. 

        # i: Tracks the index we are jumping from
        # num_jumps: Number of jumps we have taken
        i = num_jumps = 0
        
        #high: the furthest index we've already explored
        high = 0

        # we stop when we jumped to or beyond the last index
        while (i < n -1):
            num_jumps += 1

            # early stopping if the current index is the last index or above (we have reached the end)
            if max_jump >= n  - 1:
                break

            # only process from high 
            for j in range(high + 1, max_jump+1):
                candidate = j + nums[j]
                if candidate > max_jump:
                    max_jump = candidate
                    i = j

                high = j

        return num_jumps    

            



        return 0

if __name__ == "__main__":
    solution = Solution()

    nums = [2,3,0,1,4]
    print(solution.jump(nums))
