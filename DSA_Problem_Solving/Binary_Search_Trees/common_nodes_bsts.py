'''Q1. Common Nodes in Two BST
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given two BST's A and B, return the (sum of all common nodes in both A and B) % (109 +7) .

In case there is no common node, return 0.

NOTE:

Try to do it one pass through the trees.



Problem Constraints

1 <= Number of nodes in the tree A and B <= 105

1 <= Node values <= 106



Input Format

First argument represents the root of BST A.

Second argument represents the root of BST B.



Output Format

Return an integer denoting the (sum of all common nodes in both BST's A and B) % (109 +7) .



Example Input

Input 1:

 Tree A:
    5
   / \
  2   8
   \   \
    3   15
        /
        9

 Tree B:
    7
   / \
  1  10
   \   \
    2  15
       /
      11
Input 2:

  Tree A:
    7
   / \
  1   10
   \   \
    2   15
        /
       11

 Tree B:
    7
   / \
  1  10
   \   \
    2  15
       /
      11


Example Output

Output 1:

 17
Output 2:

 46


Example Explanation

Explanation 1:

 Common Nodes are : 2, 15
 So answer is 2 + 15 = 17
Explanation 2:

 Common Nodes are : 7, 2, 1, 10, 15, 11
 So answer is 7 + 2 + 1 + 10 + 15 + 11 = 46'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def solve(self, A, B):

        arr1, arr2 = [], []

        self.traverse(A, arr1)
        self.traverse(B, arr2)

        ans = 0
        m = int(1e9+7)
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):

            if arr1[i] == arr2[j]:
                ans = (ans % m + arr1[i] % m) % m
                i += 1
                j += 1
            
            elif arr1[i] > arr2[j]:
                j += 1
            
            else:
                i += 1
        
        return ans
    
    def traverse(self, root, ans):
        if not root:
            return
        self.traverse(root.left, ans)
        if root:
            ans.append(root.val)
        self.traverse(root.right, ans)