'''Q2. Merge K Sorted Lists
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a list containing head pointers of N sorted linked lists. Merge these N given sorted linked lists and return it as one sorted list.



Problem Constraints

1 <= total number of elements in given linked lists <= 100000



Input Format

First and only argument is a list containing N head pointers.



Output Format

Return a pointer to the head of the sorted linked list after merging all the given linked lists.



Example Input

Input 1:

 1 -> 10 -> 20
 4 -> 11 -> 13
 3 -> 8 -> 9
Input 2:

 10 -> 12
 13
 5 -> 6


Example Output

Output 1:

 1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
Output 2:

 5 -> 6 -> 10 -> 12 ->13


Example Explanation

Explanation 1:

 The resulting sorted Linked List formed after merging is 1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20.
Explanation 2:

 The resulting sorted Linked List formed after merging is 5 -> 6 -> 10 -> 12 ->13.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):

        head = A[0]

        for i in range(1, len(A)):
            head = self.merge_2_lists(head, A[i])
        
        return head
    
    # Non heap solution
    def merge_2_lists(self, l1, l2):

        ans = ListNode(-1)
        dummy = ans

        t1, t2 = l1, l2

        while t1 and t2:

            if t1.val < t2.val:
                dummy.next = t1
                dummy = dummy.next
                
                t1 = t1.next
            
            else:
                dummy.next = t2
                dummy = dummy.next
                
                t2 = t2.next
        
        while t1:
            dummy.next = t1
            dummy = dummy.next
            
            t1 = t1.next

        while t2:
            dummy.next = t2
            dummy = dummy.next
            
            t2 = t2.next    

        return ans.next