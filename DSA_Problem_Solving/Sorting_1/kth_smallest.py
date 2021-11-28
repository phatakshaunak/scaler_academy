'''Q1. Kth Smallest Element
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Find the Bth smallest element in given array A .

NOTE: Users should try to solve it in <= B swaps.



Problem Constraints

1 <= |A| <= 100000

1 <= B <= min(|A|, 500)

1 <= A[i] <= 109



Input Format

First argument is vector A.

Second argument is integer B.



Output Format

Return the Bth smallest element in given array.



Example Input

Input 1:

A = [2, 1, 4, 3, 2]
B = 3
Input 2:

A = [1, 2]
B = 2


Example Output

Output 1:

 2
Output 2:

 2


Example Explanation

Explanation 1:

 3rd element after sorting is 2.
Explanation 2:

 2nd element after sorting is 2.'''

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def kthsmallest(self, A, B):
	    
	    k = 0
	    A = [i for i in A]
	    for i in range(len(A)):
	        min_ind = i
	        
	        for j in range(i+1, len(A)):
	            if A[min_ind] > A[j]:
	                min_ind = j

	        A[i], A[min_ind] = A[min_ind], A[i]
	        k += 1
	        
	        if k == B:
	            break
	    return A[k-1]