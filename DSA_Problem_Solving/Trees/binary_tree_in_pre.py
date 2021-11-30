'''Q1. Binary Tree From Inorder And Preorder
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given preorder and inorder traversal of a tree, construct the binary tree.

NOTE: You may assume that duplicates do not exist in the tree.



Problem Constraints

1 <= number of nodes <= 105



Input Format

First argument is an integer array A denoting the preorder traversal of the tree.

Second argument is an integer array B denoting the inorder traversal of the tree.



Output Format

Return the root node of the binary tree.



Example Input

Input 1:

 A = [1, 2, 3]
 B = [2, 1, 3]
Input 2:

 A = [1, 6, 2, 3]
 B = [6, 1, 3, 2]


Example Output

Output 1:

   1
  / \
 2   3
Output 2:

   1  
  / \
 6   2
    /
   3


Example Explanation

Explanation 1:

 Create the binary tree and return the root node of the tree.'''

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def buildTree(self, A, B):
        m, n = len(A), len(B)

        pre_s, pre_e = 0, m - 1
        in_s, in_e = 0, n - 1
        in_map = {}

        # Track indices of inorder elements to avoid looping and increasing the time complexity
        for j in range(n):
            in_map[B[j]] = j

        def recurse(A, pre_s, pre_e, B, in_s, in_e, in_map):
            
            # Once we exhaust all elements
            if (pre_s > pre_e) or (in_s > in_e):
                return None
            
            root = TreeNode(A[pre_s])

            # for i in range(in_s, in_e + 1):
            #     if B[i] == root.val:
            #         break

            i = in_map[root.val]
            
            # Determine the indices for preorder and inorder arrays for left and right subtrees and call the function recursively.
            root.left = recurse(A, pre_s + 1, pre_s + i - in_s, B, in_s, i - 1, in_map)
            root.right = recurse(A, pre_s + i - in_s + 1, pre_e, B, i + 1, in_e, in_map)

            return root
        
        return recurse(A, pre_s, pre_e, B, in_s, in_e, in_map)

# TC: With map O(N), with loop O(N^2) for finding the index i
# SC: O(height of tree), worst O(N) where N is the number of nodes for a skewed binary tree