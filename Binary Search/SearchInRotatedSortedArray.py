from typing import List
from functools import reduce


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # Делим на две стороны
        # Они все отсортированы, и делаем поиск по двум сторонам списка.
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            
            # Если левая сторона отсортирована
            elif nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    # Если target меньше чем mid 
                    # Двигаем налево
                    r = m - 1
                else:
                    # Если target больше чем mid 
                    # Двигаем направо
                    l = m + 1
            # Если правая сторона отсортирована
            else:
                if nums[m] <= target <= nums[r]:
                    # Если target больше чем mid 
                    # Двигаем направо
                    l = m + 1 
                elif nums[m] >= target >= nums[r]: 
                    # Если target меньше чем mid 
                    # Двигаем налево
                    r = m - 1
        return -1

if __name__ == "__main__":
    s = Solution()
    target = 0
    nums = [4,5,6,7,0,1,2]
    print(s.searchMatrix(nums, target))