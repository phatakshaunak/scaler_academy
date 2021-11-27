'''Q4. Add One To Number
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: for this problem, following are some good questions to ask :

Q : Can the input have 0's before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
A : For the purpose of this question, YES
Q : Can the output have 0's before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.


Problem Constraints

1 <= size of the array <= 1000000



Input Format

First argument is an array of digits.



Output Format

Return the array of digits after adding one.



Example Input

Input 1:

[1, 2, 3]


Example Output

Output 1:

[1, 2, 4]


Example Explanation

Explanation 1:

Given vector is [1, 2, 3].
The returned vector should be [1, 2, 4] as 123 + 1 = 124.'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        
        #If array contains all zeros
        if sum(A) == 0:
            return [1]
            
        n = len(A)
        
        msb = A[n-1] + 1
        A[n-1] = msb % 10
        carry = msb // 10
        
        for i in range(n-2,-1,-1):
            val = A[i] + carry
            A[i] = val % 10
            carry = val // 10
        
        # If there is a carry increasing a position
        if sum(A) == 0:
            ans = [0]*(n+1)
            ans[0] = carry
            return ans
        
        ind = 0
        # Remove leading zeros
        while ind < n:
            if A[ind] > 0:
                break
            ind += 1
        return A[ind:]
