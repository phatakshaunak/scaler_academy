'''Q2. BST nodes in a range
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a binary search tree of integers. You are given a range B and C.

Return the count of the number of nodes that lies in the given range.



Problem Constraints

1 <= Number of nodes in binary tree <= 100000

0 <= B < = C <= 109



Input Format

First argument is a root node of the binary tree, A.

Second argument is an integer B.

Third argument is an integer C.



Output Format

Return the count of the number of nodes that lies in the given range.



Example Input

Input 1:

            15
          /    \
        12      20
        / \    /  \
       10  14  16  27
      /
     8

     B = 12
     C = 20
Input 2:

            8
           / \
          6  21
         / \
        1   4

     B = 2
     C = 20


Example Output

Output 1:

 5
Output 2:

 3


Example Explanation

Explanation 1:

 Nodes which are in range [12, 20] are : [12, 14, 15, 20, 16]
Explanation 2:

 Nodes which are in range [2, 20] are : [8, 6, 4]'''

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

        if not A:
            return 0
        
        if A.val < B:
            # Move right as all left values are < B
            return self.solve(A.right, B, C)
        
        if A.val > C:
            # Move left as all right values are out of range > C
            return self.solve(A.left, B, C)
        
        # Go in both directions and add 1 as node is in the given range
        return 1 + self.solve(A.left, B, C) + self.solve(A.right, B, C)
    
        # def traverse(ans, root, l, r):
        #     if not root:
        #         return

        #     traverse(ans, root.left, l, r)
        #     if l <= root.val <= r:
        #         ans[0] += 1
        #         # ans.append(root.val)
        #     traverse(ans, root.right, l, r)
    
        # ans = [0]
        # traverse(ans, A, B, C)

        # return ans[0]