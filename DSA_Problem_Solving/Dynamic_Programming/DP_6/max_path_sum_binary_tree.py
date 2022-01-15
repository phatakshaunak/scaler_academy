'''Q1. Max Sum Path in Binary Tree
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a binary tree T, find the maximum path sum.

The path may start and end at any node in the tree.



Problem Constraints

1 <= Number of Nodes <= 7e4

-1000 <= Value of Node in T <= 1000



Input Format

The first and the only argument contains a pointer to the root of T, A.



Output Format

Return an integer representing the maximum sum path.



Example Input

Input 1:

  
    1
   / \
  2   3
Input 2:

       20
      /  \
   -10   20
        /  \
      -10  -50


Example Output

Output 1:

 6
Output 2:

 40


Example Explanation

Explanation 1:

     The path with maximum sum is: 2 -> 1 -> 3
Explanation 2:

     The path with maximum sum is: 20 -> 20'''

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def maxPathSum(self, A):

        global_ans = [float('-inf')]

        tmp = self.helper(A, global_ans)

        return global_ans[0]

    def helper(self, root, ans):

        if not root:
            return 0
        
        left = self.helper(root.left, ans)
        right = self.helper(root.right, ans)

        ans[0] = max(ans[0], root.val + max(left, 0) + max(right, 0))

        return root.val + max(left, right, 0)