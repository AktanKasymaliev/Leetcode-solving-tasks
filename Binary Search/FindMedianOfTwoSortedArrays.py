from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        shorter, longer = nums1, nums2
        half = total_len // 2

        if len(shorter) > len(longer):
            shorter, longer  = longer, shorter

        l, r = 0, len(shorter) - 1
        while True:
            mid_shorter = (l + r) // 2
            mid_longer = half - mid_shorter - 2

            shorter_left = shorter[mid_shorter] if mid_shorter >= 0 else float("-inf")
            shorter_right = shorter[mid_shorter + 1] if (mid_shorter+1) < len(shorter) else float("inf")
            longer_left = longer[mid_longer] if mid_longer >= 0 else float("-inf")
            longer_right = longer[mid_longer + 1] if (mid_longer+1) < len(longer) else float("inf")
            
            # Проверяем на искосок, цифра слева должна быть меньше чем справа
            if shorter_left <= longer_right and longer_left <= shorter_right:
                if total_len % 2:
                    return min(shorter_right, longer_right)
                
                return (max(shorter_left, longer_left) + min(shorter_right, longer_right)) / 2
            elif shorter_left > longer_right:
                r -= 1
            else:
                l += 1 

if __name__ == "__main__":
    s = Solution()
    nums1 = [2, 3, 4]
    nums2 = [1]
    print(s.findMedianSortedArrays(nums1, nums2))