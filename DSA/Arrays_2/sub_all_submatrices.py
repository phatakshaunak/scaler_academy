'''Q1. Sum of all Submatrices
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a 2D Matrix A of dimensions N*N, we need to return sum of all possible submatrices.



Problem Constraints

1 <= N <=30

0 <= A[i][j] <= 10



Input Format

Single argument representing a 2-D array A of size N x N.



Output Format

Return an integer denoting the sum of all possible submatrices in the given matrix.



Example Input

A = [ [1, 1]
      [1, 1] ]


Example Output

16


Example Explanation

Number of submatrices with 1 elements = 4, so sum of all such submatrices = 4 * 1 = 4
Number of submatrices with 2 elements = 4, so sum of all such submatrices = 4 * 2 = 8
Number of submatrices with 3 elements = 0
Number of submatrices with 4 elements = 1, so sum of such submatrix = 4
Total Sum = 4+8+4 = 16'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        
        ans = 0
        r = len(A)
        c = len(A[0])
        for i in range(r):
            
            for j in range(c):
                
                cont = (i+1)*(j+1)*(r-i)*(c-j)*A[i][j]
                
                ans += cont
        
        return ans
