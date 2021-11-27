'''Q4. Copy List
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

A linked list A is given such that each node contains an additional random pointer which could point to any node in the list or NULL.

Return a deep copy of the list.



Problem Constraints

0 <= |A| <= 106



Input Format

The first argument of input contains a pointer to the head of linked list A.



Output Format

Return a pointer to the head of the required linked list.



Example Input

Given list
   1 -> 2 -> 3
with random pointers going from
  1 -> 3
  2 -> 1
  3 -> 1
  


Example Output

   1 -> 2 -> 3
with random pointers going from
  1 -> 3
  2 -> 1
  3 -> 1
  


Example Explanation

You should return a deep copy of the list. The returned answer should not contain the same node as the original list, but a copy of them. The pointers in the returned list should not link to any node in the original input list.'''

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):

        curr = head

        # Add new nodes equal to original node values after each old node
        while curr:
            tmp = RandomListNode(curr.label)
            tmp.next = curr.next
            curr.next = tmp
            curr = curr.next.next
        
        ans = head.next

        l1, l2 = head, ans

        # Link random nodes for the copied list
        while l1:
            
            # In case random node is null
            if not l1.random:
                l2.random = None
            else:
                l2.random = l1.random.next
            
            # When at the final node where l2.next is None
            if not l2.next:
                l2 = l2.next
            else:
                l2 = l2.next.next
            
            l1 = l1.next.next

        # Unlink connections between old and copied list
        l1, l2 = head, ans

        while l1:

            l1.next = l2.next
            
            # If l2 is at the last node in the modified list which points to null
            if not l2.next:
                l2.next = l2.next
            else:
                l2.next = l2.next.next
            
            l1 = l1.next
            l2 = l2.next

        return ans