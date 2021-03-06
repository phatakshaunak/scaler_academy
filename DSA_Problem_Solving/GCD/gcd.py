'''Q1. Greatest Common Divisor
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given 2 non negative integers A and B, find gcd(A, B)

GCD of 2 integers A and B is defined as the greatest integer g such that g is a divisor of both A and B. Both A and B fit in a 32 bit signed integer.

Note: DO NOT USE LIBRARY FUNCTIONS.



Problem Constraints

0 <= A, B <= 109



Input Format

First argument is an integer A.
Second argument is an integer B.



Output Format

Return an integer denoting the gcd(A, B).



Example Input

Input 1:

A = 4
B = 6
Input 2:

A = 6
B = 7


Example Output

Output 1:

 2
Output 2:

 1


Example Explanation

Explanation 1:

 2 divides both 4 and 6
Explanation 2:

 1 divides both 6 and 7'''

class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def gcd(self, A, B):
	    
	    while A > 0 and B > 0:
	        
	        if A >= B:
	            A = A % B
	        else:
	            B = B % A
	    
	    if A == 0:
	        return B
	    else:
	        return A
	    
	   # 6,4
	   # if A == 0:
	       # return B
	    #gcd(6,4)->gcd(4%6,6)->gcd(4,6)->gcd(6%4,4)->gcd(2,4)->gcd(4%2,2)-->gcd(0,2)
	   # return self.gcd(B%A,A)
	   # if A == 0:
    #         return B
        
    #     if B == 0:
    #         return A
        
    #     if B >=A:
    #         return self.gcd(A,B%A)
        
    #     else:
    #         return self.gcd(B,A%B)