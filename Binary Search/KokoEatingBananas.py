import math
from typing import List


class Solution:
    """
    Input: piles = [30,11,23,4,20], h = 5
    Output: 30
    She eats 30 bananas per hour, and she is in time to 
    eat all these piles with this speed(30 banana per hour)
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        What is the minimal time is required to eat all 
        piles of banana in less than or equal to "h"? 

        We take biggest num from piles and make range
        We provide binary search in this range,
        We take the smallest num from our counting,
            and it must be less or equal than "h"
        """
        l, r = 1, max(piles)
        res = r
        while l < r:
            mid = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)

            if hours <= h:
                res = min(res, mid)   
                r = mid - 1
            else:
                l = mid + 1
        return res

if __name__ == "__main__":
    s = Solution()
    piles = [30,11,23,4,20]
    h = 5
    print(s.minEatingSpeed(piles, h))