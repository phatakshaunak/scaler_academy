'''Q2. Intersection Of Sorted Arrays
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Find the intersection of two sorted arrays. OR in other words, Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example:

Input:
    A: [1 2 3 3 4 5 6]
    B: [3 3 5]

Output: [3 3 5]

Input:
    A: [1 2 3 3 4 5 6]
    B: [3 5]

Output: [3 5]
note : For the purpose of this problem ( as also conveyed by the sample case ), assume that elements that appear more than once in both arrays should be included multiple times in the final output.'''

class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return a list of integers
	def intersect(self, A, B):
	    
	    i, j =0, 0
	    ans = []
	    
	    while (i < len(A)) and (j < len(B)):
	        
	        if A[i] == B[j]:
	            ans.append(A[i])
	            i += 1
	            j += 1
	        
	        elif A[i] < B[j]:
	            i += 1
	        
	        else:
	            j += 1
	    
	    return ans

# O(m+n) time, O(1) space 