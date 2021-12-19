'''Q3. Kth Smallest Element in a Sorted Matrix
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a sorted matrix of integers A of size N x M and an integer B.

Each of the rows and columns of matrix A are sorted in ascending order, find the Bth smallest element in the matrix.

NOTE: Return The Bth smallest element in the sorted order, not the Bth distinct element.



Problem Constraints

1 <= N, M <= 500

1 <= A[i] <= 109

1 <= B <= N * M



Input Format

The first argument given is the integer matrix A.
The second argument given is an integer B.



Output Format

Return the B-th smallest element in the matrix.



Example Input

Input 1:

 A = [ [9, 11, 15],
       [10, 15, 17] ] 
 B = 6
Input 2:

 A = [  [5, 9, 11],
        [9, 11, 13],
        [10, 12, 15],
        [13, 14, 16],
        [16, 20, 21] ]
 B = 12


Example Output

Output 1:

 17
Output 2:

 16


Example Explanation

Explanation 1:

 6th smallest element in the sorted matrix is 17.
Explanation 2:

 12th smallest element in the sorted matrix is 16.'''

import heapq
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        # Make a min heap with the first column of the matrix and maintain row column indices
        # Then pop the minimum value and append the next value from the same row as the popped element.
        # Do this B times

        row, col = len(A), len(A[0])

        tmp = []

        for i in range(row):
            tmp.append((A[i][0], i, 0))
        
        heapq.heapify(tmp)

        while B > 0:
            val, r, c = heapq.heappop(tmp)

            # Add an element for the same row as top as long as the row has not been processed
            if (c + 1) < col:
                heapq.heappush(tmp, (A[r][c+1], r, c + 1))
            
            B -= 1
        
        return val
    
    # TC: O(row) to generate heap, O(B) number of pop and push operations, pop, push takes log(row), O(row) + O(B * log row) --> O(B * log row)