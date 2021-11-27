'''Q1. Find duplicate rows in a binary matrix
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Given a binary matrix A of integers 0 and 1, of size N x M.

Find and return the indices of the rows which are duplicate of rows which are already present in the matrix.

If row[i] and row[j] are same and i < j then answer will contain only index j.

Note: Rows are numbered from top to bottom and columns are numbered from left to right. There will be at least one duplicate row in the matrix.


Input Format

The first argument given is the integer matrix A.
Output Format

Return the indices of the rows in the form of an integer array.
Constraints

2 <= N, M <= 1000
0 <= A[i] <= 1
For Example

Input 1:
    A = [   [1, 0, 0]
            [0, 1, 0]
            [0, 1, 0]   ]
Output 1:
    [3]

Input 2:
    A = [   [1, 1, 1, 0]
            [0, 0, 0, 1]
            [1, 1, 1, 0]
            [0, 0, 0, 1]    ]
Output 2:
    [3, 4]'''

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        
        d_ind = {}
        ans = []
        R = len(A)
        C = len(A[0])
        
        for i in range(R):
            s = ''
            for j in range(C):
                s += str(A[i][j])
            if s in d_ind:
                ans.append(i+1)
            else:
                d_ind[s] = i
        
        return ans

'''
This solution considers only a single occurence of a duplicate row. If we need to return indices of the latest duplicate rows(if >2 occurences), then the indices need to be stored and updated in possibly an N/2 array as there can be a maximum of N/2 matches ?
'''