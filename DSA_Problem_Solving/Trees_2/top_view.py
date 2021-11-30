'''Q2. TOP VIEW
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a binary tree of integers denoted by root A. Return an array of integers representing the top view of the Binary tree.

Top view of a Binary Tree is a set of nodes visible when the tree is visited from top.

Return the nodes in any order.



Problem Constraints

1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 10^9



Input Format

First and only argument is head of the binary tree A.



Output Format

Return an array, representing the top view of the binary tree.



Example Input

Input 1:

 
            1
          /   \
         2    3
        / \  / \
       4   5 6  7
      /
     8 
Input 2:

 
            1
           /  \
          2    3
           \
            4
             \
              5


Example Output

Output 1:

 [1, 2, 4, 8, 3, 7]
Output 2:

 [1, 2, 3]


Example Explanation

Explanation 1:

Top view is described.
Explanation 2:

Top view is described.'''

from collections import deque
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):

        hm = {}
        ans = []
        min_val = float("inf")
        max_val = float("-inf")
        # d = 0
        q = deque([[A, 0]])

        while q:
            n = len(q)

            for i in range(n):
                top = q.popleft()
                
                if top[0].left:
                    q.append([top[0].left, top[1] - 1])
                
                if top[0].right:
                    q.append([top[0].right, top[1] + 1])
                
                # If distance is not present in the map, create a list, else append to existing list
                if top[1] not in hm:
                    hm[top[1]] = [top[0].val]
                else:
                    hm[top[1]].append(top[0].val)
                
                # Monitor minimum and maximum distance to use later for appending from low to high distance
                min_val = min(min_val, top[1])
                max_val = max(max_val, top[1])

        for i in range(min_val, max_val+1):
            ans.append(hm[i][0])
        
        return ans