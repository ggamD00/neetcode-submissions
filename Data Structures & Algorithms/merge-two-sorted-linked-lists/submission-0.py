# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        if list1.val < list2.val:
            startNode = list1
            newListNode = list1
            list1 = list1.next
        else:
            startNode = list2
            newListNode = list2
            list2 = list2.next
        
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                newListNode.next = list1
                list1 = list1.next
            else:
                newListNode.next = list2
                list2 = list2.next
            
            newListNode = newListNode.next

        if list1: newListNode.next = list1
        if list2: newListNode.next = list2
        
        return startNode
