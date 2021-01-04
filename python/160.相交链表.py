#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # lena = 0
        # lenb = 0
        # l = headA
        # while l != None:
        #     lena+=1
        #     l = l.next
        
        # l = headB
        # while l != None:
        #     lenb+=1
        #     l = l.next
        
        # pshort = None
        # plong = None

        # offset = 0
        # if lena < lenb:
        #     pshort = headA
        #     plong = headB
        #     offset = lenb-lena
        # else:
        #     pshort = headB
        #     plong = headA
        #     offset = lena-lenb

        # while offset > 0:
        #     offset-=1
        #     plong = plong.next

        # res = pshort
        # while plong != None:
        #     if plong != pshort:
        #         res = None
        #     else:
        #         if res == None:
        #             res = plong

        #     plong = plong.next
        #     pshort = pshort.next

        # return res
        if not headA or not headB:
            return None
        
        nodeA = headA
        nodeB = headB

        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        
        return nodeA
            
# @lc code=end

