'''Q3. Largest BST Subtree
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a Binary Tree A with N nodes.

Write a function that returns the size of the largest subtree which is also a Binary Search Tree (BST).

If the complete Binary Tree is BST, then return the size of whole tree.

NOTE:

Largest subtree means subtree with most number of nodes.


Problem Constraints

1 <= N <= 105



Input Format

First and only argument is an pointer to root of the binary tree A.



Output Format

Return an single integer denoting the size of the largest subtree which is also a BST.



Example Input

Input 1:

     10
    / \
   5  15
  / \   \ 
 1   8   7
Input 2:

     5
    / \
   3   8
  / \ / \
 1  4 7  9


Example Output

Output 1:

 3
Output 2:

 7


Example Explanation

Explanation 1:

 Largest BST subtree is
                            5
                           / \
                          1   8
Explanation 2:

 Given binary tree itself is BST.'''

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

        self.helper(A, ans)

        return ans[0]
    
    def helper(self, root, ans):

        if not root:
            return info(float('inf'), float('-inf'), 0, True)
        
        left = self.helper(root.left, ans)
        right = self.helper(root.right, ans)
        
        # Check if left and right are valid, as well as if the current tree can be a bst
        if left.is_valid and right.is_valid and root.val > left.max_ and root.val < right.min_:
            # Update ans and return the results
            node = 1 + left.nodes + right.nodes
            ans[0] = max(ans[0], node)
            return info(min(root.val, left.min_), max(root.val, right.max_), node, True)

        else:
            return info(float('inf'), float('-inf'), 0, False) # No valid BST possible beyond this point, simply return a default value

class info:
    def __init__(self, min_, max_, nodes, is_valid):
        self.min_ = min_
        self.max_ = max_
        self.nodes = nodes
        self.is_valid = is_valid