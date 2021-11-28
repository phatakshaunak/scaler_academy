'''Q5. Powers of 3
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a positive integer A. Return an array of minimum length whose elements represent the powers of 3 and the sum of all the elements is equal to A.



Problem Constraints

1 <= A <= 109



Input Format

Single argument is an integer A.



Output Format

Return an array of minimum length of powers of 3 whose elements sums to A.



Example Input

Input 1:

 13
Input 2:

 3


Example Output

Output 1:

 [1, 3, 9]
Output 2:

 [3]


Example Explanation

Explanation 1:

 30 = 1, 31 = 3, 32 = 9.
 Also, 1 + 3 + 9 = 13. Here A = 13 which can be represented as the sum of 1, 3 and 9.'''

class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        
        power = 1
        ans = []
        
        while A >= 1:
            
            rem = (A % 3)
            
            if rem == 1:
                ans.append(power)
                power *= 3
                
            elif rem == 2:
                ans.append(power)
                ans.append(power)
                power *= 3
            
            else:
                power *= 3
            
            A = A // 3
        
        return ans