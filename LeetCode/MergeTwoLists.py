# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode()
        final_node = final
        while list1 and list2:
            if list1.val > list2.val:
                final_node.next = ListNode(list2.val)
                list2 = list2.next
            else:
                final_node.next = ListNode(list1.val)
                list1 = list1.next
            final_node = final_node.next
        if list1:
            final_node.next = list1
        elif list2:
            final_node.next = list2
        return final.next