from typing import List

class Solution:
    """
    Мы аппендим температуру если она меньше чем впереди стоящего
    И stack пустой.
    Иначе если стек не пустой и температура больше позади стоящего
    Мы удаляем позади стоящего, и вычисляем расстояние между 
    текущим значением и только что удалившего значения.
    и так далее.
    
    [75(4),71(2),69(1),72(3),76(0),73(0)]
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for indx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_index = stack.pop()[-1]
                res[stack_index] = (indx - stack_index)
            stack.append([temp, indx])
        return res

if __name__ == "__main__":
    s = Solution()
    temp = [75,71,69,72,76,73]
    print(s.dailyTemperatures(temp))