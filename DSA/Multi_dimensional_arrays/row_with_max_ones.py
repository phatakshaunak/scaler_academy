'''Q5. Row with maximum number of ones
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a binary sorted matrix A of size N x N. Find the row with the maximum number of 1.

NOTE:

If two rows have the maximum number of 1 then return the row which has a lower index.
Rows are numbered from top to bottom and columns are numbered from left to right.
Assume 0-based indexing.
Assume each row to be sorted by values.
Expected time complexity is O(rows).


Problem Constraints

1 <= N <= 1000

0 <= A[i] <= 1



Input Format

The only argument given is the integer matrix A.



Output Format

Return the row with the maximum number of 1.



Example Input

Input 1:

 A = [   [0, 1, 1]
         [0, 0, 1]
         [0, 1, 1]   ]
Input 2:

 A = [   [0, 0, 0, 0]
         [0, 1, 1, 1]    ]


Example Output

Output 1:

 0
Output 2:

 1


Example Explanation

Explanation 1:

 Row 0 has maximum number of 1s.
Explanation 2:

 Row 1 has maximum number of 1s.'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        
        N = len(A) - 1
        
        # for i in range(len(A)):
            
        #     if A[i][0] == 1:
        #         return i
                
        #     # index = i
            
        #     while col >= 0 and A[i][col] == 1:
                
        #         col -= 1
        #         index = i
        
        r = 0
        col = N
        while r <= N and col >= 0:
            
            if A[r][col] == 1:
                col -= 1
                index = r
            else:
                r += 1
                
        return index