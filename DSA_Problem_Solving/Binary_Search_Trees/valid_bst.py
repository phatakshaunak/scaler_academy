'''Q2. Valid Binary Search Tree
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a binary tree represented by root A.

Assume a BST is defined as follows:

1) The left subtree of a node contains only nodes with keys less than the node's key.

2) The right subtree of a node contains only nodes with keys greater than the node's key.

3) Both the left and right subtrees must also be binary search trees.



Problem Constraints

1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 10^9



Input Format

First and only argument is head of the binary tree A.



Output Format

Return 0 if false and 1 if true.



Example Input

Input 1:

 
   1
  /  \
 2    3
Input 2:

 
  2
 / \
1   3


Example Output

Output 1:

 0
Output 2:

 1


Example Explanation

Explanation 1:

 2 is not less than 1 but is in left subtree of 1.
Explanation 2:

Satisfies all conditions.'''

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isValidBST(self, A):

        return 1 if self.preorder(A, min_ = float('-inf'), max_ = float('inf')) else 0
    
    def preorder(self, A, min_ = float('-inf'), max_ = float('inf')):

        # In order approach

        if not A:
            return True # Null is a valid BST
        
        # Check for invalid condition
        if A.val <= min_ or A.val >= max_:
            return False
        
        # Check both trees
        return self.preorder(A.left, min_, A.val) and self.preorder(A.right, A.val, max_)

#         is_valid = [1]

#         self.helper(is_valid, A)

#         return is_valid[0]
    
#     def helper(self, is_valid, root):

#         if not root:
#             return info(float('inf'), float('-inf'))

#         if is_valid[0]:

#             left = self.helper(is_valid, root.left)
#             right = self.helper(is_valid, root.right)

#             # Check if not valid (assuming unique elements in a binary tree)
#             if root.val <= left.max_ or root.val >= right.min_:
#                 is_valid[0] = 0
            
#             return info(min(root.val, left.min_), max(root.val, right.max_))
        
#         else:
#             # Return anything, it won't be checked
#             return info(-1,-1)


# class info:
#     def __init__(self, min_, max_):
#         self.min_ = min_
#         self.max_ = max_