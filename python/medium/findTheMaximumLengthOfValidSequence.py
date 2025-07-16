from typing import List


def maximumLength(nums:List[int]):
    res = 0 # initialize result variable
    # [0,0] both even
    # [0,1] one even, one odd
    # [1,0] one odd, one even
    # [1,1] both odd
    


    for pattern in [[0,0], [0,1],[1,0],[1,1]]: # scan through all patterns
        cnt = 0
        for num in nums:
            if num % 2 == pattern[cnt % 2]:
                cnt += 1
        
        res = max(res, cnt)

    return res


n = [1,2,3,4,5]
print(maximumLength(n))
