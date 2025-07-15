from typing import List

def countQuadruplets(nums: List[int]) -> int:

    n = len(nums) # 5 

    # fixiate on one of the numbers nums = [1,2,3,4,5]
    #                                       ^          ( in the first run )

    #[1,3,2,4,5]
    # 0,1,2,3,4  < - indexes

    #[1,3,2,4]

    window = 4

    for i in range(n):
        
        if i + window > n:
            break

        left_pointer = i
        right_pointer = i + window - 1
        print(f"Checking window from index {left_pointer} to {right_pointer}")

        for j in range(left_pointer, right_pointer + 1):
            print(f'value at index {j} is {nums[j]}')
            

        

        
    return 0 

if __name__ == "__main__":
    nums = [1, 3, 2, 4, 5]
    print(countQuadruplets(nums))  # Example usage
    # Expected output: 2 (quadruplets: (1, 2, 3, 4), (1, 2, 3, 5))
