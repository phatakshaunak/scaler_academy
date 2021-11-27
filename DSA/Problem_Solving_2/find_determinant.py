'''Q2. Find Determinant
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given an N X N(where N = 2 or N = 3) 2D integer matrix A. You have to find the value of its determinant (det(A) or |A|).

image

image



Problem Constraints

N = 2 or N = 3

-100 <= A[i][j] <= 100



Input Format

First and only argument is a 2D integer matrix A.



Output Format

Return an integer denoting the value of |A|.



Example Input

Input 1:

 A = [[1, 2],
      [3, 4]]
Input 2:

 A = [[6, 1, 1],
      [4, -2, 5],
      [2, 8, 7]]


Example Output

Output 1:

 -2 
Output 2:

 -306 


Example Explanation

Explanation 1:

 |A| = 1 * 4 - 2 * 3 = 4 - 6 = -2
Explanation 2:

 |A| = 6 * ((-2) * 7 - 5 * 8) - 1 * (4 * 7 - 5 * 2) + 1 * (4 * 8 - (-2) * 2) = -306'''

class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        
        if len(A) == 2:
            return (A[0][0]*A[1][1]) - (A[0][1]*A[1][0])
        
        else:
            
            sum1 = A[0][0] * ((A[1][1]*A[2][2])- (A[2][1]*A[1][2]))
            
            sum2 = A[0][1] * ((A[1][0]*A[2][2])- (A[1][2]*A[2][0]))
            
            sum3 = A[0][2] * ((A[1][0]*A[2][1])- (A[1][1]*A[2][0]))
            
            return sum1 - sum2 + sum3
            
'''There can be a recursive solution as well for a square NXN matrix'''