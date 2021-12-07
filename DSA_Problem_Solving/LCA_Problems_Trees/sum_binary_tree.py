'''Q1. Sum binary tree or not
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a binary tree. Check whether the given tree is a Sum-binary Tree or not.

Sum-binary Tree is a Binary Tree where the value of a every node is equal to sum of the nodes present in its left subtree and right subtree.

An empty tree is Sum-binary Tree and sum of an empty tree can be considered as 0. A leaf node is also considered as SumTree.

Return 1 if it sum-binary tree else return 0.



Problem Constraints

1 <= length of the array <= 100000

0 <= node values <= 50



Input Format

The only argument given is the root node of tree A.



Output Format

Return 1 if it is sum-binary tree else return 0.



Example Input

Input 1:

       26
     /    \
    10     3
   /  \     \
  4   6      3
Input 2:

       26
     /    \
    10     3
   /  \     \
  4   6      4


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 All leaf nodes are considered as SumTree. 
 Value of Node 10 = 4 + 6.
 Value of Node 3 = 0 + 3 
 Value of Node 26 = 20 + 6 
Explanation 2:

 Sum of left subtree and right subtree is 27 which is not equal to the value of root node which is 26.'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def hasPathSum(self, A, B):

        if not A:
            return 0

        # return 1 if self.helper(A, B, 0) else 0

        return 1 if self.helper_1(A, B) else 0
    
    def helper_1(self, A, B):

        # If null node, return 0 as that is not equal to the target
        if not A:
            return False
        
        # If at the leaf node, check if value is equal to the target
        if not A.left and not A.right:
            return A.val == B
        
        # Check both sides subtracting A.val from B when calling left or right
        return self.helper_1(A.left, B - A.val) or self.helper_1(A.right, B - A.val)

    def helper(self, A, B, curr):

        # If either root node has no child nodes or at leaf node
        if not A.left and not A.right:
            return curr + A.val == B
        
        # If both left and right are present
        elif A.left and A.right:
            return self.helper(A.left, B, curr + A.val) or self.helper(A.right, B, curr + A.val)
        
        # If only left present
        elif A.left and not A.right:
            return self.helper(A.left, B, curr + A.val)
        
        # Only right present
        else:
            return self.helper(A.right, B, curr + A.val)
    
    def helper_2(self, A, B, curr):

        # If null node, return 0 as that is not equal to the target
        if not A:
            return False
        
        # If at the leaf node, check if value is equal to the target
        if not A.left and not A.right:
            return A.val + curr == B
        
        # Check both sides subtracting A.val from B when calling left or right
        return self.helper_2(A.left, B, curr + A.val) or self.helper_2(A.right, B, curr + A.val)