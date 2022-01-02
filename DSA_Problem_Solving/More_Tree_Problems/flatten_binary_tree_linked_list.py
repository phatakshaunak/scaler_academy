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
        
        prev = [None]
        # return self.helper(A)
        # return self.recur_rev_post(A, prev)
        # return self.cons_space(A)
        
        return self.with_stack(A)

    def helper(self, root):
        # Base condition (Return null if node is None)
        if not root:
            return None
        
        # Accumulate flattened left and right subtrees
        left = self.helper(root.left)
        right = self.helper(root.right)

        # Now point root's right to left
        root.right = left

        # Make root's left as null
        root.left = None

        # Get to the end of the root and point it to R
        curr = root
        while curr.right:
            curr = curr.right
        
        # Point curr.right to R
        curr.right = right

        # Return flattened tree
        return root

# Keep returning right sub tree using a previous pointer TC O(N) and SC O(N)
    def recur_rev_post(self, root, prev):

        if not root:
            return
        
        self.recur_rev_post(root.right, prev)
        self.recur_rev_post(root.left, prev)

        root.right = prev[0]
        root.left = None
        prev[0] = root
        return root

# O(1) space , O(1) time...Morris

    def cons_space(self, root):
        curr = root

        while curr:

            if curr.left:
                tmp = curr.left

                while tmp.right:
                    tmp = tmp.right
                
                tmp.right = curr.right
                curr.right = curr.left
                curr.left = None
            
            curr = curr.right
        
        return root
    
    def with_stack(self, root):
        
        st = []

        st.append(root)

        while st:

            top = st.pop()

            if top.right:
                # Push right first as we need to attach left to the current node's right
                st.append(top.right)
            
            if top.left:
                st.append(top.left)

            # Check if stack is not empty and attach top's right to stack's top
            if st:
                top.right = st[-1]
                top.left = None

            # This approach in the while loop runs for all nodes in a root-left-right order as left is on top each time
        return root