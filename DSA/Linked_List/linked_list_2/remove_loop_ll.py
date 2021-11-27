'''Q3. Remove Loop from Linked List
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a linked list which contains some loop.

You need to find the node, which creates a loop, and break it by making the node point to NULL.



Problem Constraints

1 <= number of nodes <= 1000



Input Format

Only argument is the head of the linked list.



Output Format

return the head of the updated linked list.



Example Input

Input 1:

 
1 -> 2
^    |
| - - 
Input 2:

3 -> 2 -> 4 -> 5 -> 6
          ^         |
          |         |    
          - - - - - -


Example Output

Output 1:

 1 -> 2 -> NULL
Output 2:

 3 -> 2 -> 4 -> 5 -> 6 -> NULL


Example Explanation

Explanation 1:

 Chain of 1->2 is broken.
Explanation 2:

 Chain of 4->6 is broken.'''

 # Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):

        # Floyd's detection algorithm

        s, f = A, A
        intr = None
        prev = None
        while f and f.next:
            prev = s
            s = s.next
            f = f.next.next
            if s == f:
                intr = s
                break
        
        # No loop detected
        if not intr:
            return A
        
        # Run a pointer from start and intr and move one by one. Track a previous pointer to point to None once the intersection is reached.
        l1, l2 = A, intr
        while l1 != l2:

            l1 = l1.next
            prev = l2
            l2 = l2.next
        
        # Once out of the loop, prev should point to the start of the loop. Point prev to None and return modified list head A
        prev.next = None

        return A


        # set_ = set()

        # tmp = A

        # prev = None
        # while tmp:
        #     if tmp not in set_:
        #         set_.add(tmp)
            
        #     else:
        #         break
            
        #     prev = tmp    
        #     tmp = tmp.next

        # prev.next = None

        # return A

        # TC: O(N), SC: O(N)

        # Optimized algorithm: Floyd's Detection Algorithm (Slow, fast pointers)

        