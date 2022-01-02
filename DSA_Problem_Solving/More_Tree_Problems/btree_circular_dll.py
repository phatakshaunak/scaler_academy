'''Q4. Binary tree to Circular Doubly Linked List
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a binary tree convert it into circular doubly linked list based on the following rules:

The left and right pointers in nodes are to be used as previous and next pointers respectively in converted Circular Linked List.
The order of nodes in List must be same as Inorder of the given Binary Tree.
The first node of Inorder traversal must be the head node of the Circular List.
NOTE: You are expected to convert the binary tree into Doubly linked list in place.



Problem Constraints

1 <= Number of nodes in tree <= 100000

1 <= Value of node <= 109



Input Format

The only argument given is the root pointer of the tree, A.



Output Format

Return the head pointer of the converted circular doubly linked list.



Example Input

Input 1:

 Serialized from input of binary tree:(where 7 denotes the number of elements in serial)
    7 20 8 -1 -1 22 -1 -1 
    Binary tree is
      20 
     /  \
    8    22
    8 is the left child of 20 and 22 is the right child of 20.
Input 2:

 Serialized from input of binary tree:(where 7 denotes the number of elements in serial)
    7 10 8 -1 -1 11 -1 -1 
    Binary tree is
      10 
     /  \
    8    11
    8 is the left child of 10 and 11 is the right child of 10.


Example Output

Output 1:

     _____________
    |             |
    8 <-> 20 <-> 22
    |_____________|
Output 2:

     _____________
    |             |
    8 <-> 10 <-> 11
    |_____________|


Example Explanation

Explanation 1:

 The inorder traversal of binary tree is: [8, 20, 22]. Return the head pointer of the circular doubly linked list.
Explanation 2:

 The inorder traversal of binary tree is: [8, 10, 11]. Return the head pointer of the circular doubly linked list.'''

import sys
sys.setrecursionlimit(int(10e6))

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def solve(self, A):

        p = pointers()

        self.helper(A, p)

        # The helper function generates a DLL. Now only the left and right pointers for head and tail respectively need to be pointed to each other
        if p.tail:
            p.tail.right = p.head
        
        if p.head:
            p.head.left = p.tail
    
        return p.head

    def helper(self, root, ht):

        # This function generates a doubly linked list from a binary tree

        if not root:
            return
        
        self.helper(root.left, ht)
        
        # Mark head of the DLL as the left most node in the binary tree
        if not ht.head:
            ht.head = root
        
        # If head has already been marked, make connections between tail pointer and current node
        else:
            ht.tail.right = root
            root.left = ht.tail
        
        # Move tail pointer to next node, when head is marked, head and tail point to the same leftmost node in the binary tree
        # This inorder traversal will generate a sorted DLL for a BST
        ht.tail = root

        self.helper(root.right, ht)

class pointers:
    def __init__(self):
        self.head = None
        self.tail = None