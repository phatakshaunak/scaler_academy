'''Q3. Different Bits Sum Pairwise
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

We define f(X, Y) as number of different corresponding bits in binary representation of X and Y.
For example, f(2, 7) = 2, since binary representation of 2 and 7 are 010 and 111, respectively. The first and the third bit differ, so f(2, 7) = 2.

You are given an array of N positive integers, A1, A2 ,..., AN. Find sum of f(Ai, Aj) for all pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 109+7.



Problem Constraints

1 <= N <= 105

1 <= A[i] <= 231 - 1



Input Format

First and only argument of input contains a single integer array A.



Output Format

Return a single integer denoting the sum.



Example Input

Input 1:

 A = [1, 3, 5]
Input 2:

 A = [2, 3]


Example Output

Ouptut 1:

 8
Output 2:

 2


Example Explanation

Explanation 1:

 f(1, 1) + f(1, 3) + f(1, 5) + f(3, 1) + f(3, 3) + f(3, 5) + f(5, 1) + f(5, 3) + f(5, 5) 
 = 0 + 1 + 1 + 1 + 0 + 2 + 1 + 2 + 0 = 8
Explanation 2:

 f(2, 2) + f(2, 3) + f(3, 2) + f(3, 3) = 0 + 1 + 1 + 0 = 2
'''

class Solution:
	# @param A : list of integers
	# @return an integer
	def cntBits(self, A):
	    
	    max_bits = 0
	    max_num = max(A)
	    
	    while max_num:
	        max_bits += 1
	        max_num = max_num >> 1
	    
	    ans = 0
	    m = int(1e9+7)
	    n = len(A)
	    for i in range(max_bits+1):
	        set_bits = 0
	        for j in range(n):
	            if (A[j]>>i)&1:
	                set_bits += 1
	        ans = ans % m + (2 * set_bits % m * (n % m - set_bits % m + m) % m) % m
	       # ans = (ans + 2*set_bits*(n-set_bits)) % m
	    
	    return ans % m