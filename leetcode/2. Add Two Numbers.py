from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_str = ""
        l2_str = ""

        for i in l1:
            l1_str += str(i)

        for i in l2:
            l2_str += str(i)

        sum = int(l1_str[::-1]) + int(l2_str[::-1])

        return [int(i) for i in str(sum)[::-1]]


s = Solution()
a = s.addTwoNumbers(l1=[2, 4, 3], l2=[5, 6, 4])
print(a)
