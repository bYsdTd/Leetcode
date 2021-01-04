#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # ----------------方案1------------------
        # cur 永远是当前节点，当前节点不空的情况下
        # 当前节点的next先保存下来
        # 然后把当前节点指向pre节点
        # pre节点设置到当前节点
        # 当前节点指向之前保存的下一个

        # pre = None
        # cur = head
        # while cur != None:
        #     nex = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = nex
        
        # return pre

        # ----------------方案2------------------
        # 头插法
        # 创建一个新的头节点
        # 从旧list中一个一个取出，然后插入到新的list头节点的前面
        # head的next保存起来
        # head的next指向新list的头
        # head设置成新list的头
        # head的next 赋值给head做下一次迭代

        newHead = None
        while head:
            nex = head.next
            head.next = newHead
            newHead = head
            head = nex
        
        return newHead
# @lc code=end

