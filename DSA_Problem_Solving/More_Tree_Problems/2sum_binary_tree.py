'''Q2. 2-Sum Binary Tree
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a binary search tree A, where each node contains a positive integer, and an integer B, you have to find whether or not there exist two different nodes X and Y such that X.value + Y.value = B.

Return 1 to denote that two such nodes exist. Return 0, otherwise.



Problem Constraints

1 <= size of tree <= 100000

1 <= B <= 109



Input Format

First argument is the head of the tree A.

Second argument is the integer B.



Output Format

Return 1 if such a pair can be found, 0 otherwise.



Example Input

Input 1:

         10
         / \
        9   20

B = 19
Input 2:

 
          10
         / \
        9   20

B = 40


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 10 + 9 = 19. Hence 1 is returned.
Explanation 2:

 No such pair exists.'''

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
	def t2Sum(self, A, B):

        return 1 if self.traverse1(A, set(), B) else 0

        # arr = []

        # self.traverse(A, arr)

        # # Do the 2 sum hash map approach
        # hm = {}

        # for i in range(len(arr)):

        #     if B - arr[i] in hm:
        #         return 1
            
        #     if arr[i] not in hm:
        #         hm[arr[i]] = 1
        
        # return 0
    
    def traverse(self, root, arr):
        
        if not root:
            return
        
        arr.append(root.val)
        self.traverse(root.left, arr)
        self.traverse(root.right, arr)

    def traverse1(self, root, set_, target):

        if not root:
            return False
        
        if target - root.val in set_:
            return True
        
        set_.add(root.val)

        return self.traverse1(root.left, set_, target) or self.traverse1(root.right, set_, target)