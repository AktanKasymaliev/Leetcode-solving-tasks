from typing import List

class Solution:
    
    def maxArea(self, height: List[int]) -> int:
        """
        Using Two Pointers, I put left and end pointers,
        And start calculate max area with: 
            'min height between the pointers * distance between the pointers'
        Calculating logic is like: 
            '7(cause it is min height of 8 and 7) * 7(cause distance between of them) = 49'
        Calculating of square of rectangle = height * widght
        """
        l, r = 0, len(height) - 1
        maxNum = 0
        while l < r:
            minHeight, diff = min(height[l], height[r]), r - l
            maxNum = max(maxNum, minHeight * diff)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            
        return maxNum

        
if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    
    print(solution.maxArea(height))
