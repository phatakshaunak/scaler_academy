'''Q3. Remove Duplicates from Sorted List
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a sorted linked list, delete all duplicates such that each element appear only once.



Problem Constraints

0 <= length of linked list <= 106



Input Format

First argument is the head pointer of the linked list.



Output Format

Return the head pointer of the linked list after removing all duplicates.



Example Input

Input 1:

 1->1->2
Input 2:

 1->1->2->3->3


Example Output

Output 1:

 1->2
Output 2:

 1->2->3


Example Explanation

Explanation 1:

 Each element appear only once in 1->2.'''
 # Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):

        # temp = A

        # while temp.next:
        #     if temp.val == temp.next.val:
        #         temp.next = temp.next.next
        #     else:
        #         temp = temp.next
        
        # return A

        temp = A

        while temp:
            
            # Keep moving next pointer ahead until unique value encountered
            while temp.next and temp.val == temp.next.val:
                temp.next = temp.next.next
            
            temp = temp.next
        
        return A