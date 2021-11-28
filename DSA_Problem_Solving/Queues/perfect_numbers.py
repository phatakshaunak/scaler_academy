'''Q2. Perfect Numbers
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer A, you have to find the Ath Perfect Number.

A Perfect Number has the following properties:

It comprises only 1 and 2.

The number of digits in a Perfect number is even.

It is a palindrome number.

For example 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not.



Problem Constraints

1 <= A <= 100000



Input Format

The only argument given is an integer A.



Output Format

Return a string that denotes the Ath Perfect Number.



Example Input

Input 1:

 A = 2
Input 2:

 A = 3


Example Output

Output 1:

 22
Output 2:

 1111


Example Explanation

Explanation 1:

First four perfect numbers are:
1. 11
2. 22
3. 1111
4. 1221
Explanation 2:

First four perfect numbers are:
1. 11
2. 22
3. 1111
4. 1221'''

from collections import deque

class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):

        q = deque(['1', '2'])

        num = 0
        
        # Generate first halves of palindrome until num reaches A. 
        while num != A:

            x = q.popleft()

            q.append(x + '1')
            q.append(x + '2')
            num += 1
        
        ans = x

        # Concatenate reverse of ans to return Ath palindrome perfect number
        for i in range(len(x) - 1, -1, -1):
            ans = ans + x[i]
        
        return ans
