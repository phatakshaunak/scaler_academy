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

        return self.space(A, B)

        # arr1, arr2 = [], []

        # self.traverse(A, arr1)
        # self.traverse(B, arr2)

        # ans = 0
        # m = int(1e9+7)
        # i, j = 0, 0

        # while i < len(arr1) and j < len(arr2):

        #     if arr1[i] == arr2[j]:
        #         ans = (ans % m + arr1[i] % m) % m
        #         i += 1
        #         j += 1
            
        #     elif arr1[i] > arr2[j]:
        #         j += 1
            
        #     else:
        #         i += 1
        
        # return ans
    
    def space(self, root1, root2):

        ans = 0
        m = int(1e9 + 7)
        s1, s2 = [], []

        c1, c2 = root1, root2
        flag = True

        while flag:
            
            # Iterating as left as possible to get elements in sorted in order
            if c1:
                s1.append(c1)
                c1 = c1.left
            
            # Iterating as left as possible to get elements in sorted in order
            elif c2:
                s2.append(c2)
                c2 = c2.left

            # Both current nodes are null here, starting point of comparing nodes with three cases, if they are equal or either is greater than the other.
            elif s1 and s2:

                c1, c2 = s1[-1], s2[-1]

                if c1.val == c2.val:
                    ans = (ans % m + c1.val % m) % m

                    s1.pop()
                    s2.pop()
                    c1 = c1.right
                    c2 = c2.right
                
                elif c1.val < c2.val:
                    # Get next element in c1's tree, make c2 None to avoid traversing further in c2's tree
                    s1.pop()
                    c1 = c1.right
                    c2 = None
                
                elif c1.val > c2.val:
                    # Get next element in c2's tree, make c1 None to avoid traversing further in c1's tree
                    s2.pop()
                    c2 = c2.right
                    c1 = None
            
            # Exhausted either or both the trees
            else:
                
                flag = False
        
        return ans

    def traverse(self, root, ans):
        if not root:
            return
        self.traverse(root.left, ans)
        if root:
            ans.append(root.val)
        self.traverse(root.right, ans)