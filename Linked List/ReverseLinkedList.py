from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head
        # P.S next - это ссылка на след объект в LL

        # Пока список не закончился работаем!
        while current:
            # Промежуточная переменая которая меняется 
            next_ = current.next 

            # Идет смещение next -> previous т.е 
            # мы перемещаемя next назад не ломая цепь LL
            current.next = previous 
            # Смена поинтеров previous -> current; current -> next
            previous = current 
            current = next_
        return previous

# Output of head: 
    #ListNode{
    # val: 1, 
    # next: 
    #   ListNode{
    #       val: 2, 
    #       next: 
    #          ListNode{
    #               val: 3, 
    #               next: 
    #                  ListNode{
    #                       val: 4, 
    #                       next: 
    #                          ListNode{
    #                               val: 5, 
    #                               next: None
    #                   }
    #               }
    #           }
    #       }
    # }

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    solution = Solution()
    LL = ListNode()

    print(solution.reverseList(LL))
