from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1

if __name__ == "__main__":
    s = Solution()
    target = 0
    nums = [4,5,6,7,0,1,2]
    print(s.search(nums, target))