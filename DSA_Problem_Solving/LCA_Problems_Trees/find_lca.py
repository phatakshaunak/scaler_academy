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

        lca_node = [None]

        sum_ = self.recursive_lca(A, B, C, lca_node)

        # Edge case when B and C are equal and are present in the tree
        if sum_ == 1 and B == C:
            return B

        # Edge Case when both are not in the tree
        if not lca_node[0]:
            return -1
        
        return lca_node[0].val

    def recursive_lca(self, root, u, v, lca_node):

        if not root:
            return 0
        
        left = self.recursive_lca(root.left, u, v, lca_node)
        right = self.recursive_lca(root.right, u, v, lca_node)
        
        # Add a 1 if either of B and C is found in the tree
        if root.val == u or root.val == v:
            sum_ = 1 + left + right
        else:
            # Simply add results from left and right if root.val != B or root.val != C
            sum_ = left + right
        
        # If the sum is 2 and lca node is not set, the current node is the lca. Then simply update the ans. This case will then not be checked again as lca_node[0] will not be None
        if sum_ == 2 and not lca_node[0]:
            lca_node[0] = root
        
        return sum_
    
    # The recursive approach will take an O(h) space for the recursion stack, TC O(N)

    # Another approach involves finding the root to node path for both nodes and then iterating over them to find the last common node between the two

    # def lca(self, A, B, C):

    #     # Get paths for both nodes
    #     p1, p2 = [], []

    #     out1 = self.find_path(A, B, p1)
    #     out2 = self.find_path(A, C, p2)

    #     # If either return value is False, either or both not in the tree. Return False
    #     if not out1 or not out2:
    #         return -1
        
    #     # Now iterate and find last common element
    #     n, m = len(p1), len(p2)
    #     i, j = 0, 0

    #     while i < n and j < m:

    #         if p1[i] != p2[j]:
    #             break
            
    #         i += 1
    #         j += 1
        
    #     # Return previous element
    #     return p2[j-1]

    def find_path(self, root, key, path):

        # Base Case, if null return False
        if not root:
            return False
        
        # Append value
        path.append(root.val)

        # If value is the key, return True
        if root.val == key:
            return True
        
        # Check if either left or right contain the key
        if self.find_path(root.left, key, path) or self.find_path(root.right, key, path):
            # As path is found return True
            return True
        # At this point, key is not found, thus pop of the root element and return False
        path.pop()
        return False