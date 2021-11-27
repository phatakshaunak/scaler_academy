'''Q1. Single Number
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
	    unq = 0
	    for i in A:
	        unq = unq ^ i
	    return unq

'''Q2. Number of 1 Bits
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Write a function that takes an integer and returns the number of 1 bits it has.


Problem Constraints

1 <= A <= 109


Input Format

First and only argument contains integer A


Output Format

Return an integer as the answer


Example Input

Input1:
11


Example Output

Output1:
3


Example Explanation

Explaination1:
11 is represented as 1011 in binary.'''

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        
        count = 0
        if A == 1:
            return 1
        
        while A > 0:
            
            if A % 2 == 1:
                count += 1
            
            A //= 2
        
        return count