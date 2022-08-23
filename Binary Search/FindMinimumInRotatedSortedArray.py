from typing import List
from functools import reduce


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        У нас есть список, где одна половина отсортирована
        и вторая половина отсортирована
        Мы берем первое значение как минимум
        И если mid > min 
        Это значит что в первой половине нечего искать и двигаемся направо
        В итоге в min до сих пор хранится первое значение в списке
        И если mid < min а оно будет так 100% 
        Mid будет самым маленьким по логике
        """
        l, r = 0, len(nums) - 1
        minNum = nums[0]

        while l <= r:
            m = (l + r) // 2

            if nums[m] > minNum or nums[m] == minNum:
                l = m + 1
            elif nums[m] < minNum:
                minNum = nums[m]
                r = m - 1
        return minNum

        # а вообще решение похоже на searchInRotatedSortedArray

if __name__ == "__main__":
    s = Solution()
    nums = [2, 1]
    print(s.findMin(nums))