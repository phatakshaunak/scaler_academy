'''Q1. Connect ropes
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A representing the length of ropes.

You need to connect these ropes into one rope. The cost of connecting two ropes is equal to the sum of their lengths.

Find and return the minimum cost to connect these ropes into one rope.



Problem Constraints

1 <= length of the array <= 100000
1 <= A[i] <= 1000



Input Format

The only argument given is the integer array A.



Output Format

Return an integer denoting the minimum cost to connect these ropes into one rope.



Example Input

Input 1:

 A = [1, 2, 3, 4, 5]
Input 2:

 A = [5, 17, 100, 11]


Example Output

Output 1:

 33
Output 2:

 182


Example Explanation

Explanation 1:

 Given array A = [1, 2, 3, 4, 5].
 Connect the ropes in the following manner:
 1 + 2 = 3
 3 + 3 = 6
 4 + 5 = 9
 6 + 9 = 15

 So, total cost  to connect the ropes into one is 3 + 6 + 9 + 15 = 33.
Explanation 2:

 Given array A = [5, 17, 100, 11].
 Connect the ropes in the following manner:
 5 + 11 = 16
 16 + 17 = 33
 33 + 100 = 133

 So, total cost  to connect the ropes into one is 16 + 33 + 133 = 182.'''

import heapq
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        

        nl = len(A) // 2 - 1

        # Heapify input
        for i in range(nl, -1, -1):
            self.down_heapify(A, i)
        
        ans = 0
        while len(A) > 1:

            tmp = self.get_min(A) + self.get_min(A)
            ans = ans + tmp
            self.hpush(A, tmp)

        return ans

        # heapq.heapify(A)

        # ans = 0

        # while len(A) > 1:
            
        #     tmp1 = heapq.heappop(A) + heapq.heappop(A)

        #     ans = ans + tmp1

        #     heapq.heappush(A, tmp1)
        
        # return ans
    
    def hpush(self, arr, k):
        # Function to insert and heapify
        arr.append(k)

        idx = len(arr) - 1
        p = (idx - 1) // 2
        while idx != 0 and arr[p] > arr[idx]:
            arr[p], arr[idx] = arr[idx], arr[p]
            idx = p
            p = (idx - 1) // 2
    
    def get_min(self, arr):

        # Removing the min element
        arr[0], arr[-1] = arr[-1], arr[0]
        ret = arr.pop()
        self.down_heapify(arr, 0)
        return ret
    
    def down_heapify(self, arr, idx):
        # Down heapify
        flag = True
        n = len(arr)

        while flag:

            mini_ = idx

            l = 2 * idx + 1
            r = 2 * idx + 2

            if l < n and arr[l] < arr[mini_]:
                mini_ = l
            
            if r < n and arr[r] < arr[mini_]:
                mini_ = r
            
            if mini_ != idx:
                arr[idx], arr[mini_] = arr[mini_], arr[idx]
                idx = mini_
            
            else:
                flag = False