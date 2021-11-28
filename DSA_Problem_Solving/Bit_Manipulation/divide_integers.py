'''Q1. Divide Integers
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Divide two integers without using multiplication, division and mod operator.

Return the floor of the result of the division.

Also, consider if there can be overflow cases i.e output is greater than INT_MAX, return INT_MAX.

NOTE: INT_MAX = 2^31 - 1



Problem Constraints

-231 <= A, B <= 231-1

B!= 0



Input Format

First argument is an integer A denoting the dividend.
Second argument is an integer B denoting the divisor.



Output Format

Return an integer denoting the floor value of the division.



Example Input

Input 1:

 A = 5
 B = 2
Input 2:

 A = 7
 B = 1


Example Output

Output 1:

 2
Output 2:

 7


Example Explanation

Explanation 1:

 floor(5/2) = 2'''

class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def divide(self, A, B):

        ans = 0
        sign = 1
        
        if A < 0:
            A = A * (-1)
            sign = -1

        if B < 0:
            B = B * (-1)
            sign = 0 - sign
        
        for i in range(31, -1, -1):
            
            # Construct answer bit by bit (start testing with the highest bit finding highest power to deduct from A)

            if A - (B << i) >= 0:
                ans = ans + (1 << i)
                A = A - (B << i)

        if ans * sign > 2**31 - 1:
            return 2**31 - 1
        
        if ans * sign == -2**31:
            return -2**31

        return ans * sign