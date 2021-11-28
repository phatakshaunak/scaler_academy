'''Q3. Find nth Magic Number
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer A, find and return the Ath magic number.

A magic number is defined as a number which can be expressed as a power of 5 or sum of unique powers of 5.

First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….



Problem Constraints

1 <= A <= 5000



Input Format

The only argument given is integer A.



Output Format

Return the Ath magic number.



Example Input

Example Input 1:

 A = 3
Example Input 2:

 A = 10


Example Output

Example Output 1:

 30
Example Output 2:

 650


Example Explanation

Explanation 1:

 A in increasing order is [5, 25, 30, 125, 130, ...]
 3rd element in this is 30
Explanation 2:

 In the sequence shown in explanation 1, 10th element will be 650.'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        
        ans = 0
        val = 5
        while A != 0:
            if A % 2:
                ans += (A % 2) * val
            val *= 5
            A = A // 2
        
        return ans
''' 1  1 1*5
            2 10 0*5 + 1*5*5 = 25
            3 11 1*5 + 1*25 = 30
            4 100
           '''