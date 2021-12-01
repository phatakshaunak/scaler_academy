'''Q1. Identical Binary Trees
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given two binary trees, check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.



Problem Constraints

1 <= number of nodes <= 105



Input Format

First argument is a root node of first tree, A.

Second argument is a root node of second tree, B.



Output Format

Return 0 / 1 ( 0 for false, 1 for true ) for this problem.



Example Input

Input 1:

   1       1
  / \     / \
 2   3   2   3
Input 2:

   1       1
  / \     / \
 2   3   3   3


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 Both trees are structurally identical and the nodes have the same value.
Explanation 2:

 Value of left child of the tree is different.'''

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : root node of tree
	# @return an integer
	def isSameTree(self, A, B):

        # When both reach null
        if not A and not B:
            return 1

        # When one of the trees does not match
        if not A or not B:
            return 0
        
        # Compare the values and recursively call left and right sub trees for both. Return and of these operations
        left = self.isSameTree(A.left,B.left)
        right = self.isSameTree(A.right, B.right)
        return 1 if (A.val == B.val and left and right) else 0