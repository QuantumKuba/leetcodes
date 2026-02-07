from typing import List

class Solution:
    # def finalPrices(self, prices: List[int]) -> List[int]:
    #     result = prices
    #     for i in range(len(prices)):
    #         for j in range(i+1, len(prices)):
    #             if prices[i] >= prices[j]:
    #                 result[i] = prices[i] - prices[j]
    #                 break
    #     return result

    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices # make a copy of prices
        stack = [0] # stack to store the indices of the prices that are greater than the current price
        i = 1 # current index


        # untill end of the array
        while (i < len(prices)):
            # while stack is not empty and the price at the top of the stack is greater than or equal to the current price
            while(len(stack) != 0 and prices[stack[-1]] >= prices[i]):
                # apply the discount to the pirce at the top of the stack vs the current index and add it to the result
                result[stack[-1]] = prices[stack[-1]] - prices[i]
                # pop the index from the stack because we found the next smaller element
                stack.pop()

            # push the current index to the stack
            stack.append(i)
            # increment the current index
            i+=1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.finalPrices([8, 4, 6, 2, 3]))