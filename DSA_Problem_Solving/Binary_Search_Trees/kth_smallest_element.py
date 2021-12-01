'''Q4. Kth Smallest Element In Tree
Unsolved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a binary search tree represented by root A, write a function to find the Bth smallest element in the tree.



Problem Constraints

1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 10^9



Input Format

First and only argument is head of the binary tree A.



Output Format

Return an integer, representing the Bth element.



Example Input

Input 1:

 
            2
          /   \
         1    3
B = 2
Input 2:

 
            3
           /
          2
         /
        1
B = 1



Example Output

Output 1:

 2
Output 2:

 1


Example Explanation

Explanation 1:

2nd element is 2.
Explanation 2:

1st element is 1.'''

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
	def kthsmallest(self, A, B):
        # An inorder traversal returns elements in a sorted order in a BST. Simply do the traversal and 
        # return the Bth smallest element when B hits zero.`
        curr = A
        st = []

        while curr or st:

            if curr:
                # Append to the stack as we need to go left until null
                st.append(curr)
                curr = curr.left
            else:
                top = st.pop()
                B = B - 1
                if B == 0:
                    return top.val
                curr = top.right

# TC O(N), SC O(n)