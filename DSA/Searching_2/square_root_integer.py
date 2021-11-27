'''Q2. Square Root of Integer
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer A.

Compute and return the square root of A.

If A is not a perfect square, return floor(sqrt(A)).

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY.

NOTE: Do not use sort function from standard library. Users are expected to solve this in O(log(A)) time.



Problem Constraints

0 <= A <= 1010



Input Format

The first and only argument given is the integer A.



Output Format

Return floor(sqrt(A))



Example Input

Input 1:

 11
Input 2:

 9


Example Output

Output 1:

 3
Output 2:

 3


Example Explanation

Explanation:

 When A = 11 , square root of A = 3.316. It is not a perfect square so we return the floor which is 3.
 When A = 9 which is a perfect square of 3, so we return 3.'''

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        
        s, e, ans = 0, A, -1
        
        while s <= e:
            
            mid = s + (e - s) // 2
            
            if mid * mid == A:
                return mid
            elif mid * mid < A:
                ans = mid
                s = mid + 1
            else:
                e = mid - 1
        
        return ans