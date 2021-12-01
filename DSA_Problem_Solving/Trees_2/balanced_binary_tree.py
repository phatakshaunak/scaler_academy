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

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isBalanced(self, A):

        def post_order(root):

            # Base condition, if null return -1 denoting height and True as empty node is balanced
            if not root:
                return info(-1, True)

            left = post_order(root.left)
            right = post_order(root.right)

            # Check if heights condition is satisfied as well as left and right sub trees are balanced
            if abs(left.h - right.h) <= 1 and left.bal and right.bal:
                return info(1 + max(left.h, right.h), True)
            
            # Else return height and False as condition is violated
            return info(1 + max(left.h, right.h), False)
        
        return 1 if post_order(A).bal else 0

class info:
    
    def __init__(self, h, bal):
        self.h = h
        self.bal = bal