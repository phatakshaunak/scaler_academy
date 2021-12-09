'''Q1. Symmetric Binary Tree
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).



Problem Constraints

1 <= number of nodes <= 105



Input Format

First and only argument is the root node of the binary tree.



Output Format

Return 0 / 1 ( 0 for false, 1 for true ).



Example Input

Input 1:

    1
   / \
  2   2
 / \ / \
3  4 4  3
Input 2:

    1
   / \
  2   2
   \   \
   3    3


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 The above binary tree is symmetric. 
Explanation 2:

The above binary tree is not symmetric.'''

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isSymmetric(self, A):

        if not A:
            return 1
        
        return 1 if self.helper(A.left, A.right) else 0
    
    def helper(self, tree1, tree2):

        # If both null, return True
        if not tree1 and not tree2:
            return True
        
        # If either is null, return False as values do not match
        if not tree1 or not tree2:
            return False
        
        # For symmetry, root values should match as well as one tree's left and the other's right and vice versa
        # also match
        left = self.helper(tree1.left, tree2.right)
        right = self.helper(tree1.right, tree2.left)

        # Check if values match and left and right return True
        return tree1.val == tree2.val and left and right