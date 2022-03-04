'''Q1. Palindrome List
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a singly linked list A, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.



Problem Constraints

1 <= |A| <= 105



Input Format

The first and the only argument of input contains a pointer to the head of the given linked list.



Output Format

Return 0, if the linked list is not a palindrome.

Return 1, if the linked list is a palindrome.



Example Input

Input 1:

A = [1, 2, 2, 1]
Input 2:

A = [1, 3, 2]


Example Output

Output 1:

 1 
Output 2:

 0 


Example Explanation

Explanation 1:

 The first linked list is a palindrome as [1, 2, 2, 1] is equal to its reversed form.
Explanation 2:

 The second linked list is not a palindrom as [1, 3, 2] is not equal to [2, 3, 1].
'''

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return an integer
	def lPalin(self, A):

        s, f = A, A
        s_p = None
        even = False

        while f and f.next:

            if not f.next.next:
                even = True

            f = f.next.next
            s_p = s
            s = s.next
        
        if even:
            # s_p is the point where we cut off first half
            right = s_p.next
            s_p.next = None
        
        else:
            right = s.next
            s.next = None
        
        # Reverse the right half
        prev = None
        curr = right
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        left = A
        # Now right becomes prev
        right = prev

        # Iterate through both halves. For the case of odd, right list will end first,
        # For even, both lists end up at the same time
        while left and right:
            if left.val != right.val:
                return 0
            left = left.next
            right = right.next
        
        return 1

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):

        s, e = A, A
        prev = None
        
        while e and e.next:
            prev = s
            s = s.next
            e = e.next.next
        
        # If LL is of odd length, move s forward from the middle node
        if e:
            s = s.next
        
        # Single element in LL
        if not prev:
            return 1

        prev.next = None

        # A is left half to be reversed, s is the right half
        curr = A
        prev = None
        
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        l, r = prev, s
        
#         return l, r
        while l and r:
            if l.val != r.val:
                return 0
            l, r = l.next, r.next
        
        if not l and not r:
            return 1
        
        return 0
        