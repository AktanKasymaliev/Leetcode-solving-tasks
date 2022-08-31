from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pass
    
if __name__ == "__main__":
    s = Solution()
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    print(
        s.carFleet(
            target=target,
            position=position,
            speed=speed
        )
    )