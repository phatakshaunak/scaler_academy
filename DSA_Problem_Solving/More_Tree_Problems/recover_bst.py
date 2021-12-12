'''Q1. Recover Binary Search Tree
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description
Two elements of a binary search tree (BST),represented by root A are swapped by mistake. Tell us the 2 values swapping which the tree will be restored.

A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?



Problem Constraints
1 <= size of tree <= 100000



Input Format
First and only argument is the head of the tree,A



Output Format
Return the 2 elements which need to be swapped.



Example Input
Input 1:

 
         1
        / \
       2   3
Input 2:

 
         2
        / \
       3   1



Example Output
Output 1:

 [2, 1]
Output 2:

 [3, 1]


Example Explanation
Explanation 1:

Swapping 1 and 2 will change the BST to be 
         2
        / \
       1   3
which is a valid BST 
Explanation 2:

Swapping 1 and 3 will change the BST to be 
         2
        / \
       1   3
which is a valid BST'''

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers

    # Morris Traversal O(1) space
	def recoverTree(self, A):
        curr = A
        miss = []
        prev = TreeNode(float('-inf'))
        while curr:
            
            if curr.left:
                # First find predecessor
                pred = self.find_inpred(curr)
                    # Check if it is not already linked
                if not pred.right:
                    # Create the link and move left
                    pred.right = curr
                    curr = curr.left
                else:
                    #print root, cut the link and go right
                    pred.right = None    
                    
                    if curr.val < prev.val:
                        # Inversion
                        miss.append([prev, curr])
                    
                    prev = curr
                    curr = curr.right
            else:
                # Print data and go right
                
                if curr.val < prev.val:
                        # Inversion
                        miss.append([prev, curr])
                    
                prev = curr
                    
                curr = curr.right
        
        # miss[0][0].val, miss[-1][1].val = miss[-1][1].val, miss[0][0].val
        # return sorted([miss[0][0].val, miss[-1][1].val])

        return [miss[-1][1].val, miss[0][0].val]

    def find_inpred(self, root):
        tmp = root.left
        # First condition when inorder predecessor is not linked, second condition when its linked and
        # we reach the root node again.
        while tmp.right and tmp.right != root:
            tmp = tmp.right
        return tmp
    
    # O(N) space
    def recoverTree(self, A):

        B = []
        self.inorder(A, B)

        f, m, l = -1, -1, -1

        for i in range(1, len(B)):
            
            if B[i] < B[i-1]:
                if f == -1 and m == -1:
                    f = B[i-1]
                    m = B[i]
                else:
                    l = B[i]
        
        if l == -1:
            return [m, f]
        
        return [l, f]
    
    def inorder(self, root, arr):

        if not root:
            return
        
        self.inorder(root.left, arr)
        if root:
            arr.append(root.val)
        self.inorder(root.right, arr)
