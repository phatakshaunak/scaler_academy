'''Q3. RECTANGLE SUM
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a matrix of integers A of size N x M.

Calculate the sum of all submatrices and return the maximum among all those sums.

NOTE: Empty submatrix also need to be considered.



Problem Constraints

1 <= N, M <= 100
-10000 <= A[i] <= 10000



Input Format

The first and only argument given is the integer matrix A.



Output Format

Return the maximum sum among all those sums of all possible submatrices.



Example Input

Input 1:

 A = [
       [1, 3, -2]
       [1, 4, 6]
       [-4, -2, 1] 
     ]
Input 2:

 
A = [  
      [-1, -1]
      [-1, -1] 
    ]


Example Output

Output 1:

 13
Output 2:

 0


Example Explanation

Explanation 1:

 Submatrix giving maximum sum is : 
    [ 
       [1, 3, -2]
       [1, 4, 6]
    ]
Explanation 2:

 Sum of empty submatrix will be 0.'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        # Use two pointers to explore all combinations of columns, fix a left pointer, sweep R to the end and do for all starting L values from 0 to column length

        n, m = len(A), len(A[0])

        gl = 0
        matrix_max = float('-inf')
        tmp = [0 for i in range(n)]

        for L in range(m):

            for R in range(L, m):

                for row in range(n):

                    tmp[row] += A[row][R]
                    
                    matrix_max = max(matrix_max, A[row][R])
                
                # Apply Kadane's Algorithm for current column sized submatrices
                gl = max(gl, self.kadane(tmp))
            
            # At this point, all submatrices with L fixed have been explored. Reset tmp to 0
            for i in range(n):
                tmp[i] = 0
        
        # if gl == 0:
        #     return matrix_max
        
        return gl
    
    # TC: O(row^2 * column) ~ cubic, SC: O(row)

    def kadane(self, arr):

        l, g, n = 0, 0, len(arr)

        for i in range(n):

            l = max(arr[i], l + arr[i])
            g = max(g, l)
        
        # if g == 0:
        #     return max(arr)
        
        return g