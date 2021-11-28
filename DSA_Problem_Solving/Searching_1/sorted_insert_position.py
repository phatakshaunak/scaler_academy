'''Q3. Sorted Insert Position
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a sorted array A of size N and a target value B, return the index (0-based indexing) if the target is found.
If not, return the index where it would be if it were inserted in order.

NOTE: You may assume no duplicates in the array. Users are expected to solve this in O(log(N)) time.



Problem Constraints

1 <= N <= 106



Input Format

First argument is an integer array A of size N.
Second argument is an integer B.



Output Format

Return an integer denoting the index of target value.



Example Input

Input 1:

A = [1, 3, 5, 6]
 B = 5
Input 2:

A = [1]
 B = 1


Example Output

Output 1:

2
Output 2:

0


Example Explanation

Explanation 1:

The target value is present at index 2.
Explanation 2:

The target value is present at index 0.'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        
        # Recursive
        def binary_search_r(arr,s,e,val):
            
            if s > e:
                return s
            
            mid = (s + e) // 2
            
            if arr[mid] == val:
                return mid
            
            elif arr[mid] > val:
                return binary_search_r(arr,s,mid-1,val)
            
            else:
                return binary_search_r(arr, mid+1,e,val)
                
        # Iterative    
        def binary_search(arr,x):
            
            s, e = 0, len(arr)-1
            
            while s <= e:
                
                mid = (s + e) // 2
                    
                if A[mid] == x:
                    return mid
                
                elif A[mid] > x:
                    e = mid - 1
                
                else:
                    s = mid + 1
                    
            return s # If not in the array, the target value should be at this position assuming array is in ascending order
        
        # return binary_search(A,B)
        N = len(A)
        return binary_search_r(A, 0, N-1, B)