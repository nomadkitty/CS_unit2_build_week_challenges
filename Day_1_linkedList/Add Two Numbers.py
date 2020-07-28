'''
Leet code link: https://leetcode.com/problems/add-two-numbers/
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # idea
        # create a new node list with the 1st node the sum of l1 and l2's value

        # get the initial sum value
        sum = l1.val + l2.val
        # calculate initial carry
        carry = int(sum / 10)

        # create a new linked list with the initial value % 10
        new_list = ListNode(sum % 10)
        # set pointer to next nodes on l1 and l2
        l1 = l1.next
        l2 = l2.next
        # keep track of the nodes
        curr_node = new_list
        # loop through l1 and l2 while either of them is not None
        while l1 is not None or l2 is not None:
            # sum has 3 parts: carry and l1 & l2's values
            sum = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            # carry is the integer when sum divide 10
            carry = int(sum/10)
            # create the next node with the sum value % 10
            curr_node.next = ListNode(sum % 10)
            # move all 3 pointers: curr_node, l1, l2
            curr_node = curr_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # when carry is 1
        if(carry > 0):
            # create a new next node with carry
            curr_node.next = ListNode(carry)

        return new_list
