from typing import List
from functools import reduce


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = list(
            reduce(
                (lambda r, y: r + y),
                matrix
            )
        )
        l, r = 0, len(rows) - 1
        while l <= r:
            m = (l + r) // 2
            
            if rows[m] == target:
                return True
            elif rows[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False

if __name__ == "__main__":
    s = Solution()
    target = 3
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(s.searchMatrix(matrix, target))