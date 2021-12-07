'''Q3. Equal Tree Partition
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a binary tree A. Check whether it is possible to partition the tree to two trees which have equal sum of values after removing exactly one edge on the original tree.



Problem Constraints

1 <= size of tree <= 100000

-109 <= value of node <= 109



Input Format

First and only argument is head of tree A.



Output Format

Return 1 if the tree can be partitioned into two trees of equal sum else return 0.



Example Input

Input 1:

 
                5
               /  \
              3    7
             / \  / \
            4  6  5  6
Input 2:

 
                1
               / \
              2   10
                  / \
                 20  2


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 Remove edge between 5(root node) and 7: 
        Tree 1 =                                               Tree 2 =
                        5                                                     7
                       /                                                     / \
                      3                                                     5   6    
                     / \
                    4   6
        Sum of Tree 1 = Sum of Tree 2 = 18
Explanation 2:

 The given Tree cannot be partitioned.'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        
        flag = [False]

        sum_ = self.getSum(A) # O(N) 

        ans = self.post_helper(A, flag, sum_) # O(N) checking traversing to each node only once

        return 1 if flag[0] else 0

        # st = []
        # global_sum = self.sum_(A, st)
        # st.pop()

        # if global_sum // 2 in st:
        #     return 1
        
        # return 0
    
    # More concise approach that involves storing all node sums
    # def sum_(self, root, st):

    #     if not root:
    #         return 0
        
    #     left = self.sum_(root.left, st)
    #     right = self.sum_(root.right, st)

    #     st.append(root.val + left + right)

    #     return root.val + left + right

    def getSum(self, root):

        if not root:
            return 0

        return root.val + self.getSum(root.left) + self.getSum(root.right)

    def post_helper(self, root, flag, sum_):

        if not root:
            return 0
        
        left = self.post_helper(root.left, flag, sum_)
        right = self.post_helper(root.right, flag, sum_)

        # Check for equality if there is a child node to check (not applicable for a node without a child node in any branch)

        # If both nodes exist
        if root.left and root.right and (sum_ - left == left or sum_ - right == right):
            flag[0] = True
        
        # If only left exists
        elif root.left and not root.right and (sum_ - left) == left:
            flag[0] = True
        
        # If only right exists
        elif root.right and not root.left and (sum_ - right) == right:
            flag[0] = True
        
        # Return node sum to check at upper level
        return root.val + left + right