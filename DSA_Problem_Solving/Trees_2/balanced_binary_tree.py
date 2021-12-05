'''Q1. Balanced Binary Tree
Unsolved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a root of binary tree A, determine if it is height-balanced.

A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.



Problem Constraints

1 <= size of tree <= 100000



Input Format

First and only argument is the root of the tree A.



Output Format

Return 0 / 1 ( 0 for false, 1 for true ) for this problem.



Example Input

Input 1:

    1
   / \
  2   3
Input 2:

 
       1
      /
     2
    /
   3


Example Output

Output 1:

1
Output 2:

0


Example Explanation

Explanation 1:

It is a complete binary tree.
Explanation 2:

Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
Difference = 2 > 1.'''

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class info:
    def __init__(self, is_bal, height):
        self.is_bal = is_bal
        self.height = height

class Solution:
	# @param A : root node of tree
	# @return an integer

    def isBalanced(self, A):

        return self.check_ht_bal(A).is_bal
        
    def check_ht_bal(self, root):
        # Again do a post order to get results from children. Two things needed, if child node itself is balanced
        # as well as the height from left and right children. Store them in the the class info
        
        # Base condition, if a node is null, it is balanced and we can return -1 as done in the height function
        if not root:
            return info(1, -1)
        
        # Process left and right subtree as done in post order traversals
        left = self.check_ht_bal(root.left)
        right = self.check_ht_bal(root.right)
        
        # Now check two things, whether left and right are balanced as well as if the current node is height balanced
        if abs(left.height - right.height) <= 1 and left.is_bal and right.is_bal:
            # Now return an info class with true for the node being balanced and usual height calculation
            return info(1, 1 + max(left.height, right.height))
        
        # Now return False for node not balanced and usual height calculation
        return info(0, 1 + max(left.height, right.height))