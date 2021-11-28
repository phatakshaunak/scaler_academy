'''Q4. Swap List Nodes in pairs
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a linked list A, swap every two adjacent nodes and return its head.

NOTE: Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.



Problem Constraints

1 <= |A| <= 106



Input Format

The first and the only argument of input contains a pointer to the head of the given linked list.



Output Format

Return a pointer to the head of the modified linked list.



Example Input

Input 1:

 A = 1 -> 2 -> 3 -> 4
Input 2:

 A = 7 -> 2 -> 1


Example Output

Output 1:

 2 -> 1 -> 4 -> 3
Output 2:

 2 -> 7 -> 1


Example Explanation

Explanation 1:

 In the first example (1, 2) and (3, 4) are the adjacent nodes. Swapping them will result in 2 -> 1 -> 4 -> 3
Explanation 2:

 In the second example, 3rd element i.e. 1 does not have an adjacent node, so it won't be swapped. '''

 # Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        
        # Use a dummy node d to avoid edge case complications

        d = ListNode(0)

        d.next = A

        tmp = d

        while tmp.next and tmp.next.next:

            # Define pair nodes
            a = tmp.next
            b = tmp.next.next

            # Swap pairs

            # a's next goes to b's next
            a.next = b.next

            # b's next goes to a
            b.next = a

            # tmp's next goes to b
            tmp.next = b

            # Move tmp to a for next iteration
            tmp = a
        
        return d.next

        # Below approach splits the list into two lists and then merges them. This requires handles cases when list length is odd or even for either of the two lists.
        # l1, l2 = ListNode(-1), ListNode(-1)
        # t1, t2 = l1, l2
        
        # while A:

        #     t1.next = A
        #     t1 = t1.next
                
        #     A = A.next
            
        #     # For even length
        #     if A and not A.next:
        #         t1.next = None
            
        #     if A:
        #         t2.next = A
        #         A = A.next
        #         t2 = t2.next

        #         # If A is at last pointer, cut l2's last pointer, For odd length
        #         if A and not A.next:
        #             t2.next = None
        
        # ans = ListNode(-1)
        # dm = ans
        
        # l1, l2 = l1.next, l2.next

        # while l1 and l2:
            
        #     dm.next = l2
        #     dm = dm.next
        #     l2 = l2.next

        #     dm.next = l1
        #     dm = dm.next
        #     l1 = l1.next
        
        # # Remaining links in l1, if odd length list
        # if l1:
        #     dm.next = l1
        
        # return ans.next