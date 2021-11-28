'''Q4. Longest Consecutive Sequence
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an unsorted integer array A of size N.

Find the length of the longest set of consecutive elements from the array A.



Problem Constraints

1 <= N <= 106

-106 <= A[i] <= 106



Input Format

First argument is an integer array A of size N.



Output Format

Return an integer denoting the length of the longest set of consecutive elements from the array A.



Example Input

Input 1:

A = [100, 4, 200, 1, 3, 2]
Input 2:

A = [2, 1]


Example Output

Output 1:

 4
Output 2:

 2


Example Explanation

Explanation 1:

 The set of consecutive elements will be [1, 2, 3, 4].
Explanation 2:

 The set of consecutive elements will be [1, 2].'''

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestConsecutive(self, A):
	    
	    hs = set()
	    N = len(A)
	    ans = 0
	    
	    for val in A:
	        hs.add(val)
	        
	    for i in range(N):
	        
	        # This means A[i] can be the start of a consecutive element chain. Then iterate to find count of consecutive elements
	        # and then update the answer
	        if A[i] - 1 not in hs:
	            temp, flag, curr = A[i], True, 0
	            
	            while temp in hs:
	                curr += 1
	                temp += 1
	                ans = max(ans, curr)
	               # if temp not in hs:
	               #     flag = False
	               #     ans = max(ans, curr)
	            
	    return ans

