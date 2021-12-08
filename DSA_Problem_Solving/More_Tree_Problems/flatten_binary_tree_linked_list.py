'''Q4. Flatten Binary Tree to Linked List
Unsolved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a binary tree A, flatten it to a linked list in-place.

The left child of all nodes should be NULL.



Problem Constraints

1 <= size of tree <= 100000



Input Format

First and only argument is the head of tree A.



Output Format

Return the linked-list after flattening.



Example Input

Input 1:

     1
    / \
   2   3
Input 2:

         1
        / \
       2   5
      / \   \
     3   4   6


Example Output

Output 1:

1
 \
  2
   \
    3
Output 2:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6


Example Explanation

Explanation 1:

 Tree flattening looks like this.
Explanation 2:

 Tree flattening looks like this.'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):

        # Base condition (Return null if node is None)
        if not A:
            return None
        
        # Accumulate flattened left and right subtrees
        left = self.flatten(A.left)
        right = self.flatten(A.right)

        # Now point root's right to left
        A.right = left

        # Make root's left as null
        A.left = None

        # Get to the end of the root and point it to R
        curr = A
        while curr.right:
            curr = curr.right
        
        # Point curr.right to R
        curr.right = right

        # Return flattened tree
        return A