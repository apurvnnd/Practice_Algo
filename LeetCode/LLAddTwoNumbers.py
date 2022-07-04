# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_value = 0
        i=0
        while l1:
            l1_value += l1.val*(10**i)
            l1 = l1.next
            i+=1
        l2_value = 0
        i = 0
        while l2:
            l2_value+= l2.val*(10**i)
            l2=l2.next
            i+=1
        final_value = l1_value + l2_value
        final_val = ListNode()
        curr = final_val
        final_str = list(str(final_value))
        final_out = list(reversed(final_str))
        for out in final_out:
            curr.next = ListNode(int(out))
            curr = curr.next
        return final_val.next