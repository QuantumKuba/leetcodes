# Given an array of integers representing the heights, find the next person with a greater height. 

# Return an array of the people with next greater height and -1 when there is no greater height.

nums = [2,1,2,4,3]

n = len(nums)
next_greater = [-1] * n # Initialize the results array with all the persons default to -1 (no greater height)

# initialize a stack to keep track of the height of people
stack = []

# because the question is asking for next graeter height, we are going from the back. If the question was asking for the previous greater height we would be going from the front.
for i in range(n - 1, -1, -1):
    while stack and stack[-1] <= nums[i]:
        stack.pop()

    if stack:
        next_greater[i] = stack[-1]

    stack.append(nums[i])
print(next_greater)