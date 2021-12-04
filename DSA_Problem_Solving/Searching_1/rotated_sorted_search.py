'''Q2. Rotated Sorted Array Search
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a sorted array of integers A of size N and an integer B.

array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).

You are given a target value B to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

NOTE: Users are expected to solve this in O(log(N)) time.



Problem Constraints

1 <= N <= 1000000

1 <= A[i] <= 10^9

all elements in A are disitinct.



Input Format

The first argument given is the integer array A.

The second argument given is the integer B.



Output Format

Return index of B in array A, otherwise return -1



Example Input

Input 1:

A = [4, 5, 6, 7, 0, 1, 2, 3]
B = 4
Input 2:

A = [1]
B = 1


Example Output

Output 1:

 0
Output 2:

 0


Example Explanation

Explanation 1:

 
Target 4 is found at index 0 in A.
Explanation 2:

 
Target 1 is found at index 0 in A.'''

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        
        N = len(A)
        s, e = 0, (N-1)
        
        while s <= e:
            
            mid = s + (e - s) // 2
            
            if A[mid] == B:
                return mid # If you find the target, return the index
                
            if A[mid] >= A[s]: # If the left side is sorted, apply regular binary search
                
                # Check if target is in the left range
                
                if A[s] <= B < A[mid]:
                    # Move left
                    e = mid - 1
                else:
                    # Move right
                    s = mid + 1
            
            elif A[mid] <= A[e]:  # Not necessary to write this condition, an else would be fine; Here we check if the right side is sorted
                
                # Check if target is in the right range
                
                if A[mid] < B <= A[e]:
                    # Move right
                    s = mid + 1
                else:
                    # Move left
                    e = mid - 1
        
        return -1 #If not found
    
    '''
    The below approach first finds the pivot and then applies binary search on both sides. (It is still 3logN ~ log N)
    The above approach does not explicitly find the pointer. It simply modifies the regular binary search code by trying to find a sorted section and checking if the target is in that range. If yes, it discards the other section and vice versa. Thus each iteration
    removes a half similar to regular binary search without needing to find a pivot. It runs in log(N)
    '''        
    #     '''
    #         Find the pivot element. [4,5,6,7,1,2]. In a pivoted array, A[0] will always be greater than the right half (or left half in a sorted array). So, if we find that A[mid] > A[0], we know we are in the left half. Here we store mid and move right.
    #         Else move left. If the array is already sorted, the pivot will be len(A) - 1. Then apply regular binary search. Otherwise binary_search(A,x,0,pivot) and binary_search(A,x,pivot+1, length-1)
    #     '''
    #     N = len(A)
    #     l, r, pivot = 0, N - 1, -1
    
    #     while l <= r:
            
    #         mid = l + ((r - l) // 2)
            
    #         if A[mid] >= A[0]:
    #             # Equal to check if mid becomes 0
                
    #             #Store pivot and move right
    #             pivot = mid
    #             l = mid + 1
            
    #         else:
    #             r = mid - 1
        
    #     # If pivot is the end index, normal binary search
    #     if pivot == len(A) - 1:
    #         return self.binary_search(A, B, 0, N - 1)
            
    #     left = self.binary_search(A, B, 0, pivot)
    #     # right = self.binary_search(A, B, pivot + 1, N - 1)
        
    #     if left != -1:
    #         return left
        
    #     return self.binary_search(A, B, pivot + 1, N - 1)
            
    # def binary_search(self, arr, x, s, e):
        
    #     while s <= e:
            
    #         mid = s + ((e - s) // 2)
            
    #         if arr[mid] == x:
    #             return mid
                
    #         elif arr[mid] > x:
    #             e = mid - 1
            
    #         else:
    #             s = mid + 1
        
    #     return -1

    # class Solution:
    # # @param A : tuple of integers
    # # @param B : integer
    # # @return an integer
    # def search(self, A, B):

    #     s, e = 0, len(A) - 1

    #     while s <= e:
            
    #         mid = s + (e - s) // 2
    #         #If B found
    #         if A[mid] == B:
    #             return mid
            
    #         # Check if left half is sorted
    #         if A[mid] >= A[s]:
    #             # If target is within range, move left
    #             if A[s] <= B < A[mid]:
    #                 e = mid - 1
    #             else:
    #                 # Move right
    #                 s = mid + 1
            
    #         # Right half is sorted
    #         else:
    #             # If target in range, move right
    #             if A[mid] <= B < A[e]:
    #                 s = mid + 1
    #             else:
    #                 # Move left
    #                 e = mid - 1
            
    #     return -1
    
    # The algorithm tries to find a sorted section and whether the target lies in that range, If yes, move in that direction else move to the other direction.
    # This condition applies for both left and right halves
    # Another way would be to find the minimum and apply binary search on it's left and right
