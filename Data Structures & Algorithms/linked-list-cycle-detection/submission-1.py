# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        check = {}
        temp = head

        while temp != None:
            if temp in check:
                return True
            else:
                check[temp] = True
            
            temp = temp.next
        
        return False