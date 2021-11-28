'''Q4. Reverse integer
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given an integer N and the task is to reverse the digits of the given integer. Return 0 if the result overflows and does not fit in a 32 bit signed integer

Look at the example for clarification.



Problem Constraints

N belongs to the Integer limits.



Input Format

Input an Integer.



Output Format

Return a single integer denoting the reverse of the given integer.



Example Input

Input 1:

 x = 123

Input 2:

 x = -123


Example Output

Output 1:

 321

Ouput 2:

 -321


Example Explanation

 If the given integer is negative like -123 the output is also negative -321.'''

class Solution:
	# @param A : integer
	# @return an integer
	def reverse(self, A):
	    
	    if (A < 10) and (A>0):
	        return A
	    
	    sign = 1
	    
	    if A < 0:
	        A = A*(-1)
	        sign = -1
	        
	    col = 0
	    while A > 0:
	        col = (col*10) + (A%10)
            #print(col)
	        A //= 10
	    
	    if sign == -1:
	        col = col*(-1)
	        
	    if col < (-2**31) or col > 2**31:
	        return 0
	   
	    return col
        	        