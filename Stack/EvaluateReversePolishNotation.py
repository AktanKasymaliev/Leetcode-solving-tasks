from typing import List
# O(n)
class Solution:
    """
    Если мы видим оператор, то это значит мы должны 
    провести вычисления лево-стоящих цифр смотря на оператор
    и удалить их из стека, но получившееся значение мы обратно 
    добавляем в стек.
    """
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []        
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                #do act from left to right
                r, l = stack.pop(), stack.pop()
                stack.append(l - r)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                #do act from left to right
                r, l = stack.pop(), stack.pop()
                stack.append(int(l / r))
            else:
                stack.append(int(t))

        return stack.pop()

if __name__ == "__main__":
    s = Solution()
    tokens = ["2","1","+","3","*"] #output: 9
    print(s.evalRPN(tokens))