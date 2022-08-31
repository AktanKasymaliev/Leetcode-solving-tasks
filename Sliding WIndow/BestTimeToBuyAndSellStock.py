from typing import List

class Solution:
    """
    Left - Buy day, Right - Sell Day
    if l < r we calculate max profit of r - 1
    else if l > r, we just move our left pointer to right
    """

    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        l, r = 0, 1

        while len(prices)-1 >= r:
            if prices[l] < prices[r]:
                prof = max(prof, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return prof

if __name__ == "__main__":
    s = Solution()
    # prices = [7,1,5,3,6,4]
    prices = [1,2,4,2,5,7,2,4,9,0,9]
    print(
        s.maxProfit(
            prices=prices
        )
    )