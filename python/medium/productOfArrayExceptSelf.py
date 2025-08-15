from typing import List


def productExpecpSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    output = [1] * n # create an array of lenght n filled with 1's

    left = 1 
    # loop to calculate the product of all elements to the left of each index
    
    for i in range(n):
        output[i] *= left
        left *= nums[i]

    right = 1
    for i in range(n - 1, -1, -1):
        output[i] *= right 
        right *= nums[i]

    return output


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    productExpecpSelf(nums)