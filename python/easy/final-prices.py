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
        result = prices
        stack = [0]
        i = 1 

        while (i < len(prices)):
            while(len(stack) != 0 and prices[stack[-1]] >= prices[i]):
                result[stack[-1]] = prices[stack[-1]] - prices[i]

                stack.pop()

            stack.append(i)
            i+=1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.finalPrices([8, 4, 6, 2, 3]))