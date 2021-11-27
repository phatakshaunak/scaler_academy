'''Q2. K reverse linked list
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a singly linked list A and an integer B, reverse the nodes of the list B at a time and return modified linked list.



Problem Constraints

1 <= |A| <= 103

B always divides A



Input Format

The first argument of input contains a pointer to the head of the linked list.

The second arugment of input contains the integer, B.



Output Format

Return a pointer to the head of the modified linked list.



Example Input

Input 1:

 A = [1, 2, 3, 4, 5, 6]
 B = 2
Input 2:

 A = [1, 2, 3, 4, 5, 6]
 B = 3


Example Output

Output 1:

 [2, 1, 4, 3, 6, 5]
Output 2:

 [3, 2, 1, 6, 5, 4]


Example Explanation

Explanation 1:

 For the first example, the list can be reversed in groups of 2.
    [[1, 2], [3, 4], [5, 6]]
 After reversing the K-linked list
    [[2, 1], [4, 3], [6, 5]]
Explanation 2:

 For the second example, the list can be reversed in groups of 3.
    [[1, 2, 3], [4, 5, 6]]
 After reversing the K-linked list
    [[3, 2, 1], [6, 5, 4]]'''

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def reverseList(self, A, B):

        '''
        Implementation idea is similar to reversing a sub linked list in the homework.
        Since B always divides A's length, continue until curr exists reversing B nodes at a time
        If B did not always divide A's length, we could have run an outer loop len(A) // B times and then done the reversal B nodes at a time
        '''

        # Start with a dummy node and attach A to it
        d = ListNode(0)
        d.next = A
        # Use an l_prev and curr pointer pointing to d and d.next as the starting position

        l_prev, curr = d, d.next

        # Iterate until curr is not null
        while curr:

            # Define prev as None to initially point the 1st node to be reversed to null
            prev = None
            # Run a loop B times to reverse B nodes
            for i in range(B):
                # Reversal operations similar to reversing a full linked list
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # Now B nodes are reversed. We need to point 1st node (l_prev.next.next) to curr instead of null, change l_prev to l_prev.next for next set of reversal, and also point
            # l_prev.next to prev
            l = l_prev.next
            
            l_prev.next.next = curr
            l_prev.next = prev
            l_prev = l

            # return d.next
        
        return d.next
