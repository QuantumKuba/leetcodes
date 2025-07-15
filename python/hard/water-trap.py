import matplotlib.pyplot as plt
 
def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left, right = 0, len(height) - 1
    ans = 0
    left_max, right_max = 0, 0
    while left < right: # checking untill left and right pointers meet
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            ans += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            ans += right_max - height[right]
            right -= 1
    return ans



if __name__ == "__main__":
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # Output: 6
    # print(trap([4, 2, 0, 3, 2, 5]))  # Output: 9
    # print(trap([0]))  # Output: 0
    # print(trap([1, 0, 2]))  # Output: 1
    # print(trap([3, 2, 1]))  # Output: 0