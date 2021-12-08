'''Q2. Diameter of binary tree
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a Binary Tree A consisting of N integer nodes, you need to find the diameter of the tree.

The diameter of a tree is the number of edges on the longest path between two nodes in the tree.



Problem Constraints

0 <= N <= 105



Input Format

First and only Argument represents the root of binary tree A.



Output Format

Return an single integer denoting the diameter of the tree.



Example Input

Input 1:

           1
         /   \
        2     3
       / \
      4   5
Input 2:

            1
          /   \
         2     3
        / \     \
       4   5     6


Example Output

Output 1:

 3
Output 2:

 4


Example Explanation

Explanation 1:

 Longest Path in the tree is 4 -> 2 -> 1 -> 3 and the number of edges in this path is 3 so diameter is 3.
Explanation 2:

 Longest Path in the tree is 4 -> 2 -> 1 -> 3 -> 6 and the number of edges in this path is 4 so diameter is 4.'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        ans = [0]

        nodes = self.helper(A, ans)

        # As we are counting total nodes in a path, return nodes - 1 for the edges
        return ans[0] - 1
    
    def helper(self, root, ans):

        # If at null, return 0 as no nodes present
        if not root:
            return 0
        
        # Collect left and right subtrees
        left = self.helper(root.left, ans)
        right = self.helper(root.right, ans)

        # Calculate current maximum path sum
        ans[0] = max(ans[0], 1 + left + right)

        # Return max number of nodes either on left or right path of root
        return 1 + max(left, right)