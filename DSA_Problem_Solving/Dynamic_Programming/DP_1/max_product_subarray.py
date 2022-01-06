'''Q2. Max Product Subarray
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer array A of size N. Find the contiguous subarray within the given array (containing at least one number) which has the largest product.

Return an integer corresponding to the maximum product possible.

NOTE: Answer will fit in 32-bit integer value.



Problem Constraints

1 <= N <= 5 * 105

-100 <= A[i] <= 100



Input Format

First and only argument is an integer array A.



Output Format

Return an integer corresponding to the maximum product possible.



Example Input

Input 1:

 A = [4, 2, -5, 1]
Input 2:

 A = [-3, 0, -5, 0]


Example Output

Output 1:

 8
Output 2:

 0


Example Explanation

Explanation 1:

 We can choose the subarray [4, 2] such that the maximum product is 8.
Explanation 2:

 0 will be the maximum product possible.'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):

        '''
        Same as Kadane'e algorithm
        To handle negative values, keep track of local_minimum and local_maximum values ending at A[i]
        If A[i] is negative, and local_minimum is negative and local_maximum is positive, A[i] * local_minimum generates the largest product
        So keeping track of minimum and maximum local values until i-1 is necessary to find best candidate
        '''
        n = len(A)

        l_max, l_min, g_max = 1, 1, float('-inf')

        for i in range(n):
            
            tmp = max(A[i], A[i] * l_min, A[i] * l_max)
            l_min = min(A[i], A[i] * l_min, A[i] * l_max)
            l_max = tmp
            
            g_max = max(g_max, l_max)
        
        return g_max