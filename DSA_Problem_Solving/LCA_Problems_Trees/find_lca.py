'''Q1. Least Common Ancestor
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Find the lowest common ancestor in an unordered binary tree A given two values B and C in the tree.

Lowest common ancestor : the lowest common ancestor (LCA) of two nodes and w in a tree or directed acyclic graph (DAG) is the lowest (i.e. deepest) node that has both v and w as descendants.



Problem Constraints

1 <= size of tree <= 100000

1 <= B, C <= 109



Input Format

First argument is head of tree A.

Second argument is integer B.

Third argument is integer C.



Output Format

Return the LCA.



Example Input

Input 1:

 
      1
     /  \
    2    3
B = 2
C = 3
Input 2:

      1
     /  \
    2    3
   / \
  4   5
B = 4
C = 5


Example Output

Output 1:

 1
Output 2:

 2


Example Explanation

Explanation 1:

 LCA is 1.
Explanation 2:

 LCA is 2.'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):

        path1, path2 = [], []

        # u = self.find(A, path1, B)

        # v = self.find(A, path2, C)

        u = self.root_to_node(A, B, path1)

        v = self.root_to_node(A, C, path2)

        # One or both of them are not present
        if not u or not v:
            return -1
        
        # Iterate to find matching element
        i, j = 0, 0

        while i < len(path1) and j < len(path2):

            if path1[i] != path2[j]:
                break
            i += 1
            j += 1
        
        return path2[i-1]

        # Iterate to find first matching element
        # m, n = len(path1), len(path2)

        # i, j = m-1, n-1

        # while i >= 0 and j >= 0:

        #     if path1[i] != path2[j]:
        #         break
            
        #     i -= 1
        #     j -= 1
        
        # return path1[i+1]

    def root_to_node(self, root, key, path):
    
        # If null, that means key not present in the path
        if not root:
            return False
        
        # Add root data to path
        path.append(root.val)
        # Check if current node is the target
        if root.val == key:
            # Return a boolean
            return True
        # Call on left and right subtrees
        if self.root_to_node(root.left, key, path) or self.root_to_node(root.right, key, path):
            # Node present in either left or right sub tree
            return True

        # Node not present in the current root's lst or rst. Pop the node and return False
        path.pop()
        return False

    def find(self, root, path, key):

        if not root:
            return False

        if root.val == key:
            path.append(root.val)
            return True
        
        left = self.find(root.left, path, key)
        if left:
            path.append(root.val)
            return True
        
        right = self.find(root.right, path, key)
        if right:
            path.append(root.val)
            return True
        
        return False
        
            
    #     flag, ans = [True], []
    
    #     placeholder = self.helper(A, flag, ans, B, C)

    #     return ans[0]

    # def helper(self, root, flag, ans, u, v):

    #     if root == None:
    #         return 0
        
    #     # Until LCA is not found
    #     if flag[0]:
    #         left = self.helper(root.left, flag, ans, u, v)
    #         right = self.helper(root.right, flag, ans, u, v)

    #         # Check if root is the lca and one of u or v or the sum of left and right is 2 and therefore root is the lca
    #         if root.val == u or root.val == v:
                
    #             curr = 1 + left + right
            
    #             if curr == 2:
    #                 # Root itself is the answer and one of u or v
    #                 ans.append(root.val)
    #                 flag[0] = False
                
    #             # Return 1 + left + right as one of u or v is found
    #             return 1 + left + right
            
    #         # Now check if u and v originate in a different subtree and root is the lca
    #         else:
    #             if left + right == 2:
    #                 ans.append(root.val)
    #                 flag[0] = False
            
    #         # In case left + right is 0 i.e. root.val is not u or v or left + right == 1, return left + right
    #         return left + right
        
    #     else:
    #         return -1