'''Q1. Remove Nth Node from List End
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a linked list A, remove the B-th node from the end of list and return its head.

For example, Given linked list: 1->2->3->4->5, and B = 2. After removing the second node from the end, the linked list becomes 1->2->3->5.

NOTE: If B is greater than the size of the list, remove the first node of the list.

NOTE: Try doing it using constant additional space.



Problem Constraints

1 <= |A| <= 106



Input Format

The first argument of input contains a pointer to the head of the linked list.

The second argument of input contains the integer B.



Output Format

Return the head of the linked list after deleting the B-th element from the end.



Example Input

Input 1:

A = [1, 2, 3, 4, 5]
B = 2
Input 2:

A = [1]
B = 1


Example Output

Output 1:

[1, 2, 3, 5]
Output 2:

 [] 


Example Explanation

Explanation 1:

In the first example, 4 is the second last element.
Explanation 2:

In the second example, 1 is the first and the last element.'''

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def removeNthFromEnd(self, A, B):

        l, r = A, A

        # Move r such that window between l and r contains B elements
        for i in range(B - 1):
            
            # If B is greater than the length of the list, then r will point to None, if that's the case, move head pointer to A.next
            if not r.next:
                return A.next
                
            r = r.next
        
        # If after moving r, r.next is None.
        if not r.next:
            return A.next

        # Move l and r to the end storing the previous value for l. Once r hits the end, previous of l should be pointed to l.next
        prev = None
        while r.next:

            prev = l
            l = l.next
            r = r.next
        
        # For a single element, prev will still point to None
        # if not prev:
        #     return A.next

        # Point prev to l.next, bypassing Nth node from end
        prev.next = l.next
        l.next = None
        return A

    '''
    There are two edge cases for this problem:

    1. When B > length of the list ; This can be observed when the right pointer while putting it k apart from l starts pointing to None.
    2. When the list contains a single element. This will be seen if prev is still None after going through the while loop
    '''

