'''Q2. Postorder Traversal
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a binary tree, return the Postorder traversal of its nodes values.

NOTE: Using recursion is not allowed.



Problem Constraints

1 <= number of nodes <= 105



Input Format

First and only argument is root node of the binary tree, A.



Output Format

Return an integer array denoting the Postorder traversal of the given binary tree.



Example Input

Input 1:

   1
    \
     2
    /
   3
Input 2:

   1
  / \
 6   2
    /
   3


Example Output

Output 1:

 [3, 2, 1]
Output 2:

 [6, 3, 2, 1]


Example Explanation

Explanation 1:

 The Preoder Traversal of the given tree is [3, 2, 1].
Explanation 2:

 The Preoder Traversal of the given tree is [6, 3, 2, 1].'''

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def postorderTraversal(self, A):

        st = []
        ans = []
        curr = A

        while curr or st:
            
            if curr:
                ans.append(curr.val)
                st.append(curr)
                curr = curr.right
            
            else:
                curr = st[-1].left
                st.pop()
        
        i, j = 0, len(ans) - 1
        while i < j:
            ans[i], ans[j] = ans[j], ans[i]
            i += 1
            j -= 1
        
        return ans
    
    def preorderTraversal(self, A):

        st = []
        ans = []
        curr = A

        while curr or st:
            
            if curr:
                ans.append(curr.val)
                st.append(curr)
                curr = curr.left
            
            else:
                curr = st[-1].right
                st.pop()
        
        return ans
    
    def inorderTraversal(self, A):

        st = []
        ans = []
        curr = A

        while curr or st:
            
            if curr:
                st.append(curr)
                curr = curr.left
            
            else:
                ans.append(stack[-1].val)
                curr = st[-1].right
                # No need for the top node as it's left and right information has been either processed or extracted. It can be safely popped.
                st.pop()
        
        return ans

    # def postorderTraversal(self, A):
    #     ans = []
    #     self.traverse(A, ans)
    #     return ans

    # def traverse(self, A, ans):

    #     if not A:
    #         return
        
    #     self.traverse(A.left, ans)
    #     self.traverse(A.right, ans)
        
    #     if A:
    #         ans.append(A.val)
