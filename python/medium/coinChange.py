from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
       return self.recursionHelper(coins, amount)
        
    def recursionHelper(self, coins, remain):
        if remain < 0: 
            return -1
        if remain == 0:
            return 0
        
        minCount = float('inf')

        for coin in coins:
            count = self.recursionHelper(coins, remain - coin)
            if count == -1:
                continue

            minCount = min(minCount, count + 1)
            
        if minCount == float('inf'):
            return -1
        else:
            return int(minCount)
        

if __name__ == "__main__":
    s = Solution()
    coins = [1,2,5]
    amount = 11
    s.coinChange(coins, amount)