'''Q2. Add Two Numbers as Lists
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given two linked lists, A and B representing two non-negative numbers.

The digits are stored in reverse order and each of their nodes contain a single digit.

Add the two numbers and return it as a linked list.



Problem Constraints

1 <= |A|, |B| <= 105



Input Format

The first argument of input contains a pointer to the head of linked list A.

The second argument of input contains a pointer to the head of linked list B.



Output Format

Return a pointer to the head of the required linked list.



Example Input

Input 1:

 
 A = [2, 4, 3]
 B = [5, 6, 4]
Input 2:

 
 A = [9, 9]
 B = [1]


Example Output

Output 1:

 
 [7, 0, 8]
Output 2:

 
 [0, 0, 1]


Example Explanation

Explanation 1:

 A = 342 and B = 465. A + B = 807. 
Explanation 2:

 A = 99 and B = 1. A + B = 100.'''

 # Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def addTwoNumbers(self, A, B):

        l1 = ListNode(-1)

        d = l1
        carry = 0

        while A and B:

            v = A.val + B.val + carry
            curr = ListNode(v % 10)
            d.next = curr
            carry = v // 10
            d = d.next

            A, B = A.next, B.next
        
        while A:
            v = A.val + carry
            curr = ListNode(v % 10)
            d.next = curr
            carry = v // 10
            d = d.next
            A = A.next
        
        while B:
            v = B.val + carry
            curr = ListNode(v % 10)
            d.next = curr
            carry = v // 10
            d = d.next
            B = B.next
        
        if carry:
            d.next = ListNode(carry)
        
        return l1.next

        '''
        2, 4, 3
        5, 6, 4

            pl = l1.val +l2.val + carry

            carry = pl // 10
            pl = pl % 10

            prev = None
            tmp = ListNode(pl)
            tmp.next = prev
            prev = tmp

            pl = 7, carry = 0
            None <- 7

            pl, carry = 0, 1
            None <- 7 <- 0

            pl, carry = 8, 


        '''
