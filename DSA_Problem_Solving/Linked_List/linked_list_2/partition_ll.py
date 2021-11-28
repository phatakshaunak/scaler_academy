'''Q2. Partition List
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a linked list A and a value B, partition it such that all nodes less than B come before nodes greater than or equal to B.

You should preserve the original relative order of the nodes in each of the two partitions.



Problem Constraints

1 <= |A| <= 106

1 <= A[i], B <= 109



Input Format

The first argument of input contains a pointer to the head to the given linked list.

The second argument of input contains an integer, B.



Output Format

Return a pointer to the head of the modified linked list.



Example Input

Input 1:

A = [1, 4, 3, 2, 5, 2]
B = 3
Input 2:

A = [1, 2, 3, 1, 3]
B = 2


Example Output

Output 1:

[1, 2, 2, 4, 3, 5]
Output 2:

[1, 1, 2, 3, 3]


Example Explanation

Explanation 1:

 [1, 2, 2] are less than B wheread [4, 3, 5] are greater than or equal to B.
Explanation 2:

 [1, 1] are less than B wheread [2, 3, 3] are greater than or equal to B.'''

 # Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def partition(self, A, B):


        d1, d2 = ListNode(-1), ListNode(-1)

        s1, s2 = d1, d2

        l = A

        # while l:

        #     if l.val < B:
        #         s1.next = l
        #         s1 = s1.next
            
        #     else:
        #         s2.next = l
        #         s2 = s2.next
            
        #     tmp = l
        #     l = l.next
        #     tmp.next = None
        
        # s1.next = d2.next

        # return d1.next

        while l:

            if l.val < B:
                s1.next = l
                s1 = s1.next
            
            else:
                s2.next = l
                s2 = s2.next
            
            l = l.next
        
        if s1.next:
            s1.next = None
        
        if s2.next:
            s2.next = None
        
        s1 = d1

        while s1.next:
            s1 = s1.next
        
        s1.next = d2.next

        return d1.next
