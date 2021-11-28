'''Q1. Level Order
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).



Problem Constraints

1 <= number of nodes <= 105



Input Format

First and only argument is root node of the binary tree, A.



Output Format

Return a 2D integer array denoting the zigzag level order traversal of the given binary tree.



Example Input

Input 1:

    3
   / \
  9  20
    /  \
   15   7
Input 2:

   1
  / \
 6   2
    /
   3


Example Output

Output 1:

 [
   [3],
   [9, 20],
   [15, 7]
 ]
Output 2:

 [ 
   [1]
   [6, 2]
   [3]
 ]


Example Explanation

Explanation 1:

 Return the 2D array. Each row denotes the traversal of each level.'''

from collections import deque

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def levelOrder(self, A):
        
        # Get the number of levels to define size of array of arrays
        levels = self.get_ht(A)

        # Define ans array of arrays
        ans = [[] for i in range(levels + 1)]

        # Define a queue
        q = deque()

        # Initialize with the root node and initial value of zero
        q.append([A, 0])

        # Define current level as 0
        curr_level = 0

        # Fill ans
        self.fill(curr_level, q, ans)

        return ans

    def fill(self, curr_level, queue, ans):

        # Loop until queue contains nodes
        while queue:

            top = queue.popleft()
            # Enqueue children of first element if they exist and increment their level
            if top[0].left:
                queue.append([top[0].left, top[1] + 1])
            
            if top[0].right:
                queue.append([top[0].right, top[1] + 1])
            
            # Append the top element's value to the correct array
            if curr_level == top[1]:
                ans[curr_level].append(top[0].val)
            else:
                curr_level = top[1]
                ans[curr_level].append(top[0].val)
    
    def get_ht(self, A):

        if not A:
            return -1
        
        left = self.get_ht(A.left)
        right = self.get_ht(A.right)

        return 1 + max(left, right)