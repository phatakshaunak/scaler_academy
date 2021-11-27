'''Q4. Minimum Difference Puzzle
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

There is a shop whose assistant told you that there are A puzzles in the shop and you want to buy B of them. They might differ in difficulty and size. The first jigsaw puzzle consists of A1 pieces, the second one consists of A2 pieces and so on.

You decided that the difference between the numbers of pieces in bought puzzles must be as small as possible. Let x be the number of pieces in the largest puzzle that the you buy and y be the number of pieces in the smallest such puzzle. You want to choose such B puzzles that x-y is as minimum as possible. Find the least possible value of x-y.



Problem Constraints

1 <= A <= 103

1 <= B <= A

1 <= A[i] <= 106



Input Format

First argument is a vector A whose ith element represents number of pieces of ith puzzle.

Second argument is an integer B as per the question.



Output Format

Return an integer showing minimum possible value of x-y.



Example Input

Input 1:

A={10, 12, 10, 7, 5, 22}, B=4


Example Output

Output 1:

5


Example Explanation

Explanation 1:

Selected puzzles are 10, 10, 12, 7: (Max-Min) = (12-7) = 5.'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        # O(NlogN) time complexity, space O(N)
        A.sort()
        N = len(A)
        # Initialize two pointers determining the expanse of the window
        
        i = 0
        j = i + B - 1
        min_val = float("inf")
        
        while j <= (N-1):
            min_val = min(min_val, (A[j]-A[i]))
            i += 1
            j += 1
        
        return min_val
        
# Time complexity O(NlogN) due to sorting ; space complexity O(N) for sorting overhead