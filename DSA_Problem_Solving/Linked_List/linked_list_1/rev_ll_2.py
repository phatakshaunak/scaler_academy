'''Q1. Reverse Link List II
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Reverse a linked list A from position B to C.

NOTE: Do it in-place and in one-pass.

Problem Constraints

1 <= |A| <= 106

1 <= B <= C <= |A|

Input Format

The first argument contains a pointer to the head of the given linked list, A.

The second arugment contains an integer, B.

The third argument contains an integer C.

Output Format

Return a pointer to the head of the modified linked list.

Example Input

Input 1:

 A = 1 -> 2 -> 3 -> 4 -> 5
 B = 2
 C = 4

Input 2:

 A = 1 -> 2 -> 3 -> 4 -> 5
 B = 1
 C = 5

Example Output

Output 1:

 1 -> 4 -> 3 -> 2 -> 5
Output 2:

 5 -> 4 -> 3 -> 2 -> 1

Example Explanation

Explanation 1:

 In the first example, we want to reverse the highlighted part of the given linked list : 1 -> 2 -> 3 -> 4 -> 5 
 Thus, the output is 1 -> 4 -> 3 -> 2 -> 5 
Explanation 2:

 In the second example, we want to reverse the highlighted part of the given linked list : 1 -> 4 -> 3 -> 2 -> 5  
 Thus, the output is 5 -> 4 -> 3 -> 2 -> 1 '''

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @param C : integer
	# @return the head node in the linked list
	def reverseBetween(self, A, B, C):

        # Define dummy node
        d = ListNode(0)
        # Link A to it
        d.next = A

        # Define starting pointers...curr and l_prev
        curr = d
        l_prev = None

        # Iterate to lth pointer
        for i in range(B):
            l_prev = curr
            curr = curr.next
        
        # Then keep reversing until moving beyond C'th pointer, (C - B + 1) times
        # Point lth pointer (which is currently curr) to null initially and keep reversing until rth pointer is reached
        prev = None

        for j in range(C - B + 1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # Now l_prev should point to prev which is the reversed link. l_prev.next.next, the original Bth pointer should now point to curr
        
        # Change link for lth node (B)
        l_prev.next.next = curr

        # Change link for l_prev to prev (the reversed link)
        l_prev.next = prev

        return d.next