'''Q2. Vertical and Horizontal Sums
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a matrix B, of size N x M, you are allowed to do at most A special operations on this grid such that there is no vertical or horizontal contiguous subarray that has a sum greater than C.

A special operation involves multiplying any element by -1 i.e. changing its sign.

Return 1 if it is possible to achieve the answer, otherwise 0.



Problem Constraints

1 <= N, M <= 10

0 <= A <= 5

-105 <= B[i][j], C <= 105



Input Format

The first argument is an integer A, representing the number of special operations allowed.
The second argument has the N x M integer matrix, B.
The third argument is an integer C, as described in the problem statement.



Output Format

Return 1 if it is possible to achieve the answer, otherwise 0.



Example Input

Input 1:

 A = 3
 B = [  
        [1, 1, 1]
        [1, 1, 1]
        [1, 1, 1]
     ]
 C = 2
Input 2:

 A = 1
 B = [
        [1, 1, 1]
        [1, 1, 1]
        [1, 1, 1]
     ]
 C = 2


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 The given matrix does not satisfy the conditions, but if we apply the special operation to B[0][0], B[1][1], B[2][2],
 then the matrix would satisfy the given conditions i.e. no row or column has a sum greater than 2.
Explanation 2:

 It is not possible to apply the special operation to 1 element to satisfy the conditions.'''

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        # Rows
        n = len(B)
        # Columns
        m = len(B[0])
        
        return self.backtrack(A, B, C, n, m)
    
    def backtrack(self, A, B, C, n, m):
        
        # Why < 0, should be == 0?
        if A < 0:
            return 0
        
        # Set default answer; This will be updated if conditions are violated
        ans = 1
        
        # Test out all horizontal sub arrays
        
        for i in range(n):
            
            for j in range(m):
                sm = 0
                # Test out all sub arrays in the ith row. The loop below checks for all subarrays starting at A[i][j]
                for k in range(j, m):
                    sm += B[i][k]
                    if sm > C: # Call recursion for all elements in subarray between j and k
                        ans = 0 # Update the answer to 0 as condition is violated
                        
                        for s in range(j,k+1):
                            B[i][s] = 0 - B[i][s]
                            ans = ans | self.backtrack(A - 1, B, C, n, m)
                            B[i][s] = 0 - B[i][s]
                        
                        # Return statement here ensures ans is returned for all recursion calls in the above
                        # if block
                        
                        return ans
        
        # Test out all vertical sub arrays
        
        for j in range(m):
            
            for i in range(n):
                sm = 0
                # Test out all sub arrays in the jth column. The loop below checks for all subarrays starting at A[i][j]
                for k in range(i, n):
                    sm += B[k][j]
                    if sm > C: # Call recursion for all elements in subarray between i and k
                        ans = 0 # Update the answer to 0 as condition is violated
                        
                        for s1 in range(i, k+1):
                            B[s1][j] = 0 - B[s1][j]
                            ans = ans | self.backtrack(A - 1, B, C, n, m)
                            B[s1][j] = 0 - B[s1][j]
                        
                        # Return statement here ensures ans is returned for all recursion calls in the above
                        # if block
                        return ans
            
        # After all sub-arrays are exhausted, simply return the value for answer
        return ans