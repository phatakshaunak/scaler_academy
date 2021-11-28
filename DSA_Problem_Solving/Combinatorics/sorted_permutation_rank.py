'''Q1. Sorted Permutation Rank
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
Rank is clearly 1.'''

class Solution:
	# @param A : string
	# @return an integer
	def findRank(self, A):
	    
	    m = 1000003
	    N = len(A)
	    
	    def fact(num):
	        ans = 1
	        while num > 1:
	            ans = (ans % m * num % m) % m
	            num -= 1
	        return ans
	    
	    ans = 0
	    for i in range(N):
	        less = 0
	        for j in range(i+1,N):
	            if A[j] < A[i]:
	                less += 1
	        
	        ans = (ans % m + (less % m * fact(N-1-i)) % m) % m
	    
	    return ans+1
	        
'''
dcba
3*3! + 2*2! + 1*1! + 0 = 18 + 4 + 1 = 23

abcdef
dfbea
3*4! + 5*3! + 1*2! + 4*1! + 0 = 3*24 + 5*9 + 2 + 4 = 72+45+6 = 123
'''