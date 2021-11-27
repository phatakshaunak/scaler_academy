'''Q2. Minimize the absolute difference
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Given three sorted arrays A, B and Cof not necessarily same sizes.

Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively. i.e. minimize | max(a,b,c) - min(a,b,c) |.

Example :

Input:

A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]
Output:

1
Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.'''

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer
	def solve(self, A, B, C):
	    
	    i, j, k = 0, 0, 0
	    diff = float("inf")
	    
	    while (i < len(A)) and (j < len(B)) and (k < len(C)):
	        
	        n_max = max(A[i],B[j],C[k])
	        n_min = min(A[i],B[j],C[k])
	        
	        diff = min(diff, (n_max-n_min))
	        
	        if diff == 0:
	            return 0
	    
    	    # Move a pointer for any (there can be multiple minimums) minimum value forward
    	    
    	    if n_min == A[i]:
    	        i += 1
    	    
    	    elif n_min == B[j]:
    	        j += 1
    	    
    	    else:
    	        k += 1
    	    
	    return diff

'''
The brute force approach would be to just use three nested loops and consider all possible triplets. This will amount to a TC of O(n^3)
To take advantage of sorted arrays, start with the first elements. Next, we need to just increment the index for the minimum value in the triplet. With this approach, we are fixing our maximum and just trying to maximimize the minimum value.
The time complexity of this approach would be O(p+q+r) time and O(1) space where p,q and r are the lengths of the three arrays
'''