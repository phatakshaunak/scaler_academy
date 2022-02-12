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
        
        st1, st2 = [], []

        self.pushleft(A, st1)

        self.pushright(A, st2)

        left, right = self.popleft(st1), self.popright(st2)

        while left < right:
            
            curr = left + right

            if curr == B:
                return 1
            
            elif curr > B:

                # Move behind, i.e popright
                right = self.popright(st2)
            
            else:
                
                # Move forward
                left = self.popleft(st1)
        
        return 0

        # arr = []

        # self.traverse(A, arr)

        # i, j = 0, len(arr) - 1

        # while i < j:

        #     curr = arr[i] + arr[j]

        #     if curr == B:
        #         return 1
            
        #     elif curr > B:
        #         j -= 1
            
        #     else:
        #         i += 1
        
        # return 0
    
    def traverse(self, root, arr):

        if not root:
            return
        
        self.traverse(root.left, arr)
        arr.append(root.val)
        self.traverse(root.right, arr)

    def pushleft(self, root, st):

        while root:
            st.append(root)
            root = root.left

    def pushright(self, root, st):

        while root:
            st.append(root)
            root = root.right

    def popleft(self, st):

        top = st.pop()
        self.pushleft(top.right, st)
        return top.val

    def popright(self, st):

        top = st.pop()
        self.pushright(top.left, st)
        return top.val
    
    # https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/1420711/C%2B%2BJavaPython-3-solutions%3A-HashSet-Stack-Python-yield-Solutions-O(H)-space