# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1==None:
            return l2
        if l2==None:
            return l1
        merge = ListNode(-1)
        cur = merge
        
        while l1!=None and l2!=None:
            if l1.val<=l2.val:
                merge.next = l1
                l1 = l1.next
                merge = merge.next
            else:
                merge.next = l2
                l2 = l2.next
                merge = merge.next
        if l1!=None:
            merge.next =l1
        if l2!=None:
            merge.next = l2
        
        return cur.next
