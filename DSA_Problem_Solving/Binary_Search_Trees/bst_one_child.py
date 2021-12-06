'''Q3. Check for BST with One Child
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given preorder traversal of a binary tree, check if it is possible that it is also a preorder traversal of a Binary Search Tree (BST), where each internal node (non-leaf nodes) have exactly one child.



Problem Constraints

1 <= number of nodes <= 100000



Input Format

First and only argument is an integer array denoting the preorder traversal of binary tree.



Output Format

Return a string "YES" if true else "NO".



Example Input

Input 1:

 A : [4, 10, 5, 8]
Input 2:

 A : [1, 5, 6, 4]


Example Output

Output 1:

 "YES"
Output 2:

 "NO"


Example Explanation

Explanation 1:

 The possible BST is:
            4
             \
             10
             /
             5
              \
              8
Explanation 2:

 There is no possible BST which have the above preorder traversal.'''

class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):

        if not A or len(A) <= 2:
            return 'YES'

        bounds = [float('-inf'), float('inf')]

        for i in range(1, len(A)):

            if A[i] > A[i-1]:
                # A[i] is the right child, thus it should be greater than min, change min to A[i-1]
                bounds[0] = A[i -1]
            
            else:
                # A[i] is the left child, change maximum value to A[i-1]
                bounds[1] = A[i-1]
            
            # If A[i] is not within bounds, return False
            if not (bounds[0] < A[i] < bounds[1]):
                return "NO"
        
        return "YES"