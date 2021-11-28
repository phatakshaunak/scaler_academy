'''Q2. Single Number
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A, every element appears twice except for one. Find that single one.

NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?



Problem Constraints

2 <= |A| <= 2000000

0 <= A[i] <= INTMAX



Input Format

First and only argument of input contains an integer array A.



Output Format

Return a single integer denoting the single element.



Example Input

Input 1:

 A = [1, 2, 2, 3, 1]
Input 2:

 A = [1, 2, 2]


Example Output

Output 1:

 3
Output 2:

 1


Example Explanation

Explanation 1:

3 occurs once.
Explanation 2:

1 occurs once.'''

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, A):
	    
	   # # Count bit positions in max number
	   # max_num = max(A)
	    
	   # max_bits = 0
	   # while max_num > 1:
	   #     max_bits += 1
	   #     max_num //= 2
	    
	   # ans = 0
	   # for i in range(max_bits+1):
	   #     set_bits = 0
	   #     for j in range(len(A)):
	   #         if (A[j]>>i)&1:
	   #             set_bits += 1
	   #     if set_bits&1:
	   #         ans = ans + (1<<i)
	    
	   # return ans
	    
	    ans = 0
	    for num in A:
	        ans = ans ^ num
	    return ans