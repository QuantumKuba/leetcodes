import collections
from typing import List

def visibleMountains(peaks: List[List[int]]) -> int:
    stack = []
    rightMost = float('-inf')

    # Sort peaks by their x-coordinate, and in case of a tie, by their height (y-coordinate)
    for x, y in sorted(peaks):
        # these represent the start and end of the mountain (the left most and the right most points)
        start, end = x - y, x + y

        while stack and stack[-1] >= start:
            stack.pop()

        if end > rightMost:
            rightMost = end
            stack.append(start)

    return len(stack)
        

if __name__ == "__main__":
    peaks = [[2,2],[6,3],[5,4]]
    print(visibleMountains(peaks))  # Example usage
    # Expected output: Number of visible mountains based on the given peaks.