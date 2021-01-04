#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # res = None
        # cur = None
        # while l1 != None or l2 != None:
        #     if l1 == None:
        #         opNode = l2
        #         l2 = l2.next
        #     elif l2 == None:
        #         opNode = l1
        #         l1 = l1.next
        #     else:
        #         if l1.val < l2.val:
        #             opNode = l1
        #             l1 = l1.next
        #         else:
        #             opNode = l2
        #             l2 = l2.next

        #     if res == None:
        #         res = opNode
        #     else:
        #         cur.next = opNode

        #     cur = opNode

        # 双指针，新建一个头节点
        # 在两个节点都不空的情况下，每次取出当前值比较，
        # 小的拿出来插入新的list，同时指针往后移动一个
        # 结束以后，某一个是空的，那么把另一个插入最后

        pre = ListNode(-1)
        head = pre
        while l1 and l2:

            if l1.val < l2.val:
                node = l1
                l1 = l1.next
            else:
                node = l2
                l2 = l2.next

            pre.next = node
            pre = node
        
        pre.next = l1 if l1 else l2
        return head.next
            
            
        
# @lc code=end

