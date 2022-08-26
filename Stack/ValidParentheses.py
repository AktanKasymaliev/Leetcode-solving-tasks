from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Делаю pop из закрывающихся скобок стека,
        и сравниваю с открывающимися скобками i
        При таких кейсах  "((("
        Они все добавляются в стек и потом pop'аются
        в итоге если стек пустой это значит что надо False
        """
        stack = deque()

        for i in s:
            if i in "{[(":
                stack.append(i)
            elif i in "}])":
                if not stack:
                    return False

                open_brack = stack.pop()
                if open_brack == "(" and  i == ")":
                    continue
                elif open_brack == "[" and i == "]":
                    continue
                elif open_brack == "{" and i == "}":
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
            


if __name__ == "__main__":
    s = Solution()
    str_ = "[["
    print(s.isValid(str_))