'''Q3. Next Pointer Binary Tree
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a binary tree,

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Assume perfect binary tree and try to solve this in constant extra space.



Problem Constraints

1 <= Number of nodes in binary tree <= 100000

0 <= node values <= 10^9



Input Format

First and only argument is head of the binary tree A.



Output Format

Return the head of the binary tree after the changes are made.



Example Input

Input 1:

 
     1
    /  \
   2    3
Input 2:

 
        1
       /  \
      2    5
     / \  / \
    3  4  6  7


Example Output

Output 1:

 
        1 -> NULL
       /  \
      2 -> 3 -> NULL
Output 2:

 
         1 -> NULL
       /  \
      2 -> 5 -> NULL
     / \  / \
    3->4->6->7 -> NULL


Example Explanation

Explanation 1:

Next pointers are set as given in the output.
Explanation 2:

Next pointers are set as given in the output.'''

# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):

        if not root:
            return None

        temp = root

        while temp:

            curr_level = temp

            while curr_level:

                if curr_level.left and curr_level.right:
                    curr_level.left.next = curr_level.right
                
                if curr_level.next and curr_level.right:
                        curr_level.right.next = curr_level.next.left
                
                curr_level = curr_level.next
            
            temp = temp.left
        
        return root

    '''Assign next pointers of one level below from one level top. Use an outer while loop to traverse left. An inner loop is used to then traverse horizontally to point all next nodes
       at that level. Then keep traversing left until all nodes are processed.
       This is an O(N) approach with O(1) space as all nodes get visited once.
       Another simpler approach would be use a queue and then point the next nodes. This would take O(N) space
    '''