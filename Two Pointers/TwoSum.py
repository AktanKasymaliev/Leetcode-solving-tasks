from typing import List

class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        I set two points at the begining and at the end,
        add two values of pointers,
        if the sum is greather than target, we're gonna move on
        the right pointer to the lefttoward otherwise if the 
        sum is less than target, we're gonna move on the left pointer
        to the righttoward.
        """
        l, r = 0, len(numbers) - 1

        while l < r: 
            guess_sum = numbers[l] + numbers[r]
            if guess_sum == target:
                return [l+1, r+1]
            elif guess_sum > target:
                r -= 1
            elif guess_sum < target:
                l += 1
        return 
            



if __name__ == "__main__":
    numbers = [-1,0]
    target = -1
    solution = Solution()
    print(solution.twoSum(numbers, target))
