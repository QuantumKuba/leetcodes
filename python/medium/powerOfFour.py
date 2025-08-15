class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # base case, if n cant be a power of 4, return false
        if n<0:
            return False
        # incrementer
        i=0
        while True: # continue until we find a match or exceed n
            temp = 4**i # raise 4 to the power of i 
            if temp==n: # if temp is exact match to n
                return True
            elif temp>n: # if we exceeded the target
                return False
            
            i+=1

if __name__ == "__main__":
    solution = Solution()
    n = 16
    print(solution.isPowerOfFour(n))