'''Q3. NQueens
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer A, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
The final list should be generated in such a way that the indices of the queens in each list should be in reverse lexicographical order.


Problem Constraints

1 <= A <= 10



Input Format

First argument is an integer n denoting the size of chessboard



Output Format

Return an array consisting of all distinct solutions in which each element is a 2d char array representing a unique solution.



Example Input

Input 1:

A = 4
Input 2:

A = 1


Example Output

Output 1:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Output 1:

[
 [Q]
]


Example Explanation

Explanation 1:

There exist only two distinct solutions to the 4-queens puzzle:
Explanation 1:

There exist only one distinct solutions to the 1-queens puzzle:'''

class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):

        # Define a visited column array using indices as columns and values to be booleans
        cols = [0] * A

        # Diagonals and anti-diagonals 2*A - 1
        diags, anti = [0] * ((2*A) - 1), [0] * ((2*A) - 1)

        # Define grid
        curr = [['.'] * A for i in range(A)]

        ans = []

        self.backtrack(A, curr, cols, diags, anti, ans, 0)

        return ans

    def backtrack(self, A, curr, cols, diags, anti, ans, r):

        if r == A:
            ans.append([''.join(i) for i in curr])
            return
        
        for i in range(A):
            
            # Ensure valid position not in the same column or along both diagonals
            if (not cols[i]) and (not diags[r - i + A - 1]) and (not anti[r + i]):

                # Place queen
                curr[r][i] = 'Q'

                # Mark columns, diagonals and anti-diagonals
                cols[i], diags[r - i + A - 1], anti[r + i] = 1, 1, 1

                # Recurse to the next row
                self.backtrack(A, curr, cols, diags, anti, ans, r + 1)

                # Reset visited arrays and grid
                curr[r][i] = '.'
                cols[i], diags[r - i + A - 1], anti[r + i] = 0, 0, 0
