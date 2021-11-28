'''Q3. Reorder List
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a singly linked list A

 A: A0 → A1 → … → An-1 → An 
reorder it to:

 A0 → An → A1 → An-1 → A2 → An-2 → … 
You must do this in-place without altering the nodes' values.



Problem Constraints

1 <= |A| <= 106



Input Format

The first and the only argument of input contains a pointer to the head of the linked list A.



Output Format

Return a pointer to the head of the modified linked list.



Example Input

Input 1:

 A = [1, 2, 3, 4, 5] 
Input 2:

 A = [1, 2, 3, 4] 


Example Output

Output 1:

 [1, 5, 2, 4, 3] 
Output 2:

 [1, 4, 2, 3] 


Example Explanation

Explanation 1:

 The array will be arranged to [A0, An, A1, An-1, A2].
Explanation 2:

 The array will be arranged to [A0, An, A1, An-1, A2].'''

 # Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reorderList(self, A):
        
        if not A.next:
            return A
		# Define two pointers l and r same as head pointer A
		l, r = A, A

		# First find the middle of the list
		while r and r.next:
			l = l.next
			r = r.next.next
		
		# Cut the two lists at l's current location
		r = l.next

        # Modifies A
		l.next = None

		# Reverse the list r
	
		# Pointer to point to when reversing
		prev = None

		# Nodes to reverse
		curr = r
		
		while curr:

			# Store curr's next
			tmp = curr.next

			# Point curr to prev
			curr.next = prev

			# Store curr in prev for next link's reversal (i.e. tmp)
			prev = curr

			# Move curr forward
			curr = tmp
		
		# Change r to prev as head of reversed list and l to A
		r = prev
		l = A
		
		# Define dummy node and merge l and r

		ans = ListNode(None)
		dm = ans

		while l and r:
			
			# Point dm to l and r in that order, move all three forward
			dm.next = l
			l = l.next
			dm = dm.next

			dm.next = r
			r = r.next
			dm = dm.next
		
		# Add remaining elements from l1 as l1 pointer always ends at mid + 1
        dm.next = l
		
		return ans.next

# TC O(N), SC O(N)
'''
Steps followed
1. Find the middle node using slow and fast pointer approach
2. Reverse the second half
3. Connect 1st and 2nd half one by one in that order
'''