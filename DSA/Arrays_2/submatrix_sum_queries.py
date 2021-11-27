'''Q4. Sub-matrix Sum Queries
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a matrix of integers A of size N x M and multiple queries Q, for each query find and return the submatrix sum.

Inputs to queries are top left (b, c) and bottom right (d, e) indexes of submatrix whose sum is to find out.

NOTE:

Rows are numbered from top to bottom and columns are numbered from left to right.
Sum may be large so return the answer mod 109 + 7.


Problem Constraints

1 <= N, M <= 1000
-100000 <= A[i] <= 100000
1 <= Q <= 100000
1 <= B[i] <= D[i] <= N
1 <= C[i] <= E[i] <= M



Input Format

The first argument given is the integer matrix A.
The second argument given is the integer array B.
The third argument given is the integer array C.
The fourth argument given is the integer array D.
The fifth argument given is the integer array E.
(B[i], C[i]) represents the top left corner of the i'th query.
(D[i], E[i]) represents the bottom right corner of the i'th query.



Output Format

Return an integer array containing the submatrix sum for each query.



Example Input

Input 1:

 A = [   [1, 2, 3]
         [4, 5, 6]
         [7, 8, 9]   ]
 B = [1, 2]
 C = [1, 2]
 D = [2, 3]
 E = [2, 3]
Input 2:

 A = [   [5, 17, 100, 11]
         [0, 0,  2,   8]    ]
 B = [1, 1]
 C = [1, 4]
 D = [2, 2]
 E = [2, 4]


Example Output

Output 1:

 [12, 28]
Output 2:

 [22, 19]


Example Explanation

Explanation 1:

 For query 1: Submatrix contains elements: 1, 2, 4 and 5. So, their sum is 12.
 For query 2: Submatrix contains elements: 5, 6, 8 and 9. So, their sum is 28.
Explanation 2:

 For query 1: Submatrix contains elements: 5, 17, 0 and 0. So, their sum is 22.
 For query 2: Submatrix contains elements: 11 and 8. So, their sum is 19.'''

class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        
        N = len(A)
        M = len(A[0])
        mod = int(1e9+7)
        
        # Define a prefix sum matrix (Additional row and column padding helps with using the formula for the first rows and columns as 
        # there is not -1 access for the 0th element if we consider the ps array of the same length as the original array
        
        ps = [[0]*(M+1) for i in range(N+1)]
        
        # Populate prefix sum matrix
        for i in range(N):
            for j in range(M):
                ps[i+1][j+1] = (A[i][j] + ps[i+1][j] + ps[i][j+1] - ps[i][j]) % mod
                
        ans = []
        
        # Loop through the queries
        
        for i in range(len(B)):
            
            r1, c1 = B[i], C[i]
            r2, c2 = D[i], E[i]
            
            sub_sum = ps[r2][c2] - ps[r1-1][c2] - ps[r2][c1-1] + ps[r1-1][c1-1]
            
            ans.append(sub_sum % mod)
        
        return ans
        
#Time O(M*N) + O(Q) where M and N are dimensions of the input matrix and Q is the number of queries
# Space O(M*N) as we define a 2D prefix sum matrix
# Without a prefix matrix, a brute force method would involve iterating through each range and amount to time of O(Q*M*N) and space of O(1)