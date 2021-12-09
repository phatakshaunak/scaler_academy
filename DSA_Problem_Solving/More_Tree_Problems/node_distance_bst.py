'''Q3. Distance between Nodes of BST
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a binary search tree.
Return the distance between two nodes with given two keys B and C. It may be assumed that both keys exist in BST.

NOTE: Distance between two nodes is number of edges between them.



Problem Constraints

1 <= Number of nodes in binary tree <= 1000000

0 <= node values <= 109



Input Format

First argument is a root node of the binary tree, A.

Second argument is an integer B.

Third argument is an integer C.



Output Format

Return an integer denoting the distance between two nodes with given two keys B and C



Example Input

Input 1:

    
         5
       /   \
      2     8
     / \   / \
    1   4 6   11
 B = 2
 C = 11
Input 2:

    
         6
       /   \
      2     9
     / \   / \
    1   4 7   10
 B = 2
 C = 6


Example Output

Output 1:

 3
Output 2:

 1


Example Explanation

Explanation 1:

 Path between 2 and 11 is: 2 -> 5 -> 8 -> 11. Distance will be 3.
Explanation 2:

 Path between 2 and 6 is: 2 -> 6. Distance will be 1'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        # Approach involves finding the LCA and then summing the distance from LCA to B and C
        ans = [0]

        b = self.find_lca(A, B, C, ans)
        
        B_dist, C_dist = [0], [0]

        self.find_dist(ans[0], B, B_dist)
        self.find_dist(ans[0], C, C_dist)

        return B_dist[0] + C_dist[0]
    
    def find_lca(self, root, u, v, ans):

        if not root:
            return False
        
        if root.val == u or root.val == v:
            ans[0] = root
            return True
        
        if (u > root.val and v < root.val) or (u < root.val and v > root.val):
            ans[0] = root
            return True
        
        if root.val > u and root.val > v:
            return self.find_lca(root.left, u, v, ans)
        
        if root.val < u and root.val < v:
            return self.find_lca(root.right, u, v, ans)
    
    def find_dist(self, root, key, dist):

        if root.val == key:
            return
        
        elif root.val > key:
            # Go left, incrementing count
            dist[0] += 1
            self.find_dist(root.left, key, dist)
        
        else:
            # Go right, increment count
            dist[0] += 1
            self.find_dist(root.right, key, dist)