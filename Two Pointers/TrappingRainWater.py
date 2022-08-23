from typing import List

class Solution:
    
    def trap(self, height: List[int]) -> int:
        maxL = 0 
        maxR = 0
        ans = 0

        l, r = 0, len(height) - 1
        while l < r:
            if height[l] > height[r]:
                maxR = max(maxR, height[r]) # нахомдим макс справа для рассчета
                ans = ans + (maxR - height[r]) # высчитываем maxR - height[r] > 0  
                r -= 1
            elif height[l] <= height[r]:
                maxL = max(maxL, height[l]) # нахомдим макс слева для рассчета
                ans = ans + (maxL - height[l]) # высчитываем maxL - height[l] > 0  
                l += 1 
        return ans
        
if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    solution = Solution()
    
    print(solution.trap(height))
