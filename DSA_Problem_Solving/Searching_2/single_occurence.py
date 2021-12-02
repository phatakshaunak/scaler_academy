'''Q2. Single Element in a Sorted Array
Unsolved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a sorted array of integers A where every element appears twice except for one element which appears once, find and return this single element that appears only once.

note: Users are expected to solve this in O(log(N)) time.



Problem Constraints

1 <= |A| <= 100000

1 <= A[i] <= 10^9



Input Format

The only argument given is the integer array A.



Output Format

Return the single element that appears only once.



Example Input

Input 1:

A = [1, 1, 7]
Input 2:

A = [2, 3, 3]


Example Output

Output 1:

 7
Output 2:

 2


Example Explanation

Explanation 1:

 7 appears once
Explanation 2:

 2 appears once'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        if len(A) == 1:
            return A[0]
        
        s, e = 0, (len(A) - 1)
        
        #Edge cases when the non-duplicate element occurs at the start or end of the array
        
        if A[s] != A[s+1]:
            return A[s]
        
        if A[e] != A[e-1]:
            return A[e]
        
        while s <= e:
            
            mid = s + (e - s) // 2
            
            # Check if we found the unique element in any place apart from 0 or N-1
            
            if A[mid] != A[mid - 1] and A[mid] != A[mid + 1]:
                return A[mid]
                
            '''The observation here is that if duplicates occur to the left of unique element, their first occurence index is even, whereas their first occurence is odd to the right of the unique element. We need two checks for these conditions
               to decide how to reduce the search space
            '''
            # Condition for hitting the first or second occurence of an element on the left of the unique element, then move the start pointer
            
            if ((A[mid] == A[mid - 1]) and (mid & 1)) or ((A[mid] == A[mid + 1]) and ((mid - 1) & 1)):
                s = mid + 1
            
            # If we are on the right, then move the end pointer
            else:
                e = mid - 1
        
        return -1

# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, A):

#         def single_occ_bs(A):
    
#             s, e = 0, len(A) - 1
            
#             # Edge cases:
            
#             if A[0] != A[1]:
#                 return A[0]
            
#             if A[e] != A[e-1]:
#                 return A[e]
            
#             while s <= e:
                
#                 mid = s + (e - s) // 2
#         #         print('start', s, 'end',e)
#                 '''Check for single occurence element'''
                
#                 '''Conditions when mid occurs at start or end of array'''
                
#         #         if mid == 0 and A[mid] != A[mid + 1]:
#         #             return A[mid]
                
#         #         if mid == (len(A) - 1) and A[mid] != A[mid - 1]:
#         #             return A[mid]
                
#                 '''Single element occurs anywhere other than start and end'''
#                 if A[mid] != A[mid - 1] and A[mid] != A[mid + 1]:
#                     return A[mid]
                
#                 '''Next consider how to move the pointers ; We know that the first occurence index of an element to the
#                 the left of the unique element is even. Thus if we hit the 1st or 2nd occurence of an element to
#                 the left of the unique element, we need to move right.
                
#                 Else, if we hit the 1st or 2nd occurence of an element to the right, then we move left.
#                 '''
                
#                 if ((A[mid] == A[mid - 1]) and ((mid-1)%2==0)) or ((A[mid] == A[mid + 1]) and ((mid)%2==0)):
                    
#                     s = mid + 1
                
#                 else:
#                     e = mid - 1
#             return -1
    
#         return single_occ_bs(A)
