'''Q3. Sorted Permutation Rank
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a string A. Find the rank of the string amongst its permutations sorted lexicographically.
Assume that no characters are repeated.

Note: The answer might not fit in an integer, so return your answer % 1000003



Problem Constraints

1 <= |A| <= 1000



Input Format

First argument is a string A.



Output Format

Return an integer denoting the rank of the given string.



Example Input

Input 1:

A = "acb"
Input 2:

A = "a"


Example Output

Output 1:

2
Output 2:

1


Example Explanation

Explanation 1:

Given A = "acb".
The order permutations with letters 'a', 'c', and 'b' : 
abc
acb
bac
bca
cab
cba
So, the rank of A is 2.
Explanation 2:

Given A = "a".
Rank is clearly 1.
'''

class Solution:
	# @param A : string
	# @return an integer
	def findRank(self, A):
	    
	    def fact(n):
	        ans = 1
	        for i in range(1,n+1):
	            ans = (ans * i) % 1000003
	        return ans
	   
	    rank = 0
	    N = len(A)
	    for i in range(N-1):
	        count = 0
	        for j in range(i+1,N):
	            if A[j] < A[i]:
	                count += 1
	                
	        if count != 0:
	            
	            rank = (rank + (count * fact(N-i-1)% 1000003)) % 1000003
	    
	    return (rank+1) % 1000003

# Time complexity O(n^2), space complexity O(1)