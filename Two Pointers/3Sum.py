from typing import List

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        In the first I gonna sort area for no catching up duplicate,
        then our first number it will be first value of sorted area,
        then we have to find rest two values like in Two Sum taks.

        """
        # Сперва сортируем чтобы не наткнуться на дупликаты
        triplets = []
        nums.sort()

        # Первый цикл для того чтобы использовать первые цифры из списка
        # проходимся N(колво ел в списке) раз по списку и каждый раз обновляем l
        # и обновляем первое число v
        for i, v in enumerate(nums): 
            # При втором заходе в цикл необращаем внимание на дупликаты.
            # и обновляем первое число v
            if i > 0 and v == nums[i - 1]:
                continue
            
            # Второй цикл для того чтобы найти оставшиеся две цифры
            l, r = i + 1, len(nums) - 1
            while l < r:
                # Складываем и получаем 0. Если не получаемя идем по условиям 
                guess_sum = v + nums[l] + nums[r]
                # Если сумма больше чем 0 то двигаем правую налево
                if guess_sum > 0:
                    r -= 1
                # Если сумма меньше чем 0 то двигаем левую направо
                elif guess_sum < 0:
                    l += 1
                # Если нашли троицу которая дает нам 0
                else:
                    # Добавляем в список и двигаем налево
                    # Чтобы посмотреть есть ли еще троицы
                    # Короче говоря начинает цикл еще раз
                    triplets.append([
                        v, nums[l], nums[r]
                    ])
                    l += 1
                    # Двигаем налево, и смотрим чтобы дупликаты не собрали 
                    # nums[l] == nums[l - 1] and l < r Мы скипаем дупликат и переходим к селдующему
                    # двигаем направо к концу.
                    # говорим, что пока есть дупликаты и границы не закончились
                    # двигать направо и закончить цикл.
                    # В кратце говоря мы скипаем дупликаты в 53 строке)
                    
                    # + помогает в кейсах [0, 0, 0, 0]
                    # так как мы таким образом переходим к 21 строке и скипаем все
                    # без этой части кода l не двигается и список дублируется
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1 
        return triplets

if __name__ == "__main__":
    numbers = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    print(solution.threeSum(numbers))
