'''Q4. Special Median
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given an array A containing N numbers. This array is called special if it satisfies one of the following properties:

There exists an element A[i] in the array such that A[i] is equal to the median of elements [A[0], A[1], ...., A[i-1]]
There exists an element A[i] in the array such that A[i] is equal to the median of elements [A[i+1], A[i+2], ...., A[N-1]]
Median is the middle element in the sorted list of elements. If the number of elements are even then median will be (sum of both middle elements)/2.

Return 1 if the array is special else return 0.

NOTE:

For A[0] consider only the median of elements [A[1], A[2], …, A[N-1]] (as there are no elements to the left of it)
For A[N-1] consider only the median of elements [A[0], A[1], …., A[N-2]]


Problem Constraints

1 <= N <= 1000000.
A[i] is in the range of a signed 32-bit integer.



Input Format

First and only argument is an integer array A.



Output Format

Return 1 if the given array is special else return 0.



Example Input

Input 1:

 A = [4, 6, 8, 4]
Input 2:

 A = [2, 7, 3, 1]


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explantion 1:

 Here, 6 is equal to the median of [8, 4].
Explanation 2:

 No element satisfies any condition.'''

import heapq
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        if len(A) == 1:
            return 0
        # We can calculate median in a stream two ways (l to r and r to l). Then check if A[i] equals the median in either of the arrays, and return 1
    
        left = self.median_stream(A)

        right = self.median_stream(list(reversed(A)))

        right.reverse()

        # Can avoid storing the median values and check while calculating the median on each iteration.
        
        for i in range(len(A)):

            if i == 0:
                if A[i] == right[i+1]:
                    return 1
            
            elif i == len(A) - 1:
                if A[i] == left[i-1]:
                    return 1
            
            else:
                if A[i] == left[i-1] or A[i] == right[i+1]:
                    return 1
        
        return 0
            
    def median_stream(self, arr):

        # Define two heaps, max heap for the left side, min heap for the right side
        n = len(arr)
        l_max, r_min, ans = [], [], []

        for i in range(n):
            
            # Insert into min heap if it is empty or the top value is smaller than A[i]. Otherwise put in the max heap
            if not r_min or r_min[0] < arr[i]:
                heapq.heappush(r_min, arr[i])

            else:
                heapq.heappush(l_max, (-1 * arr[i]))
            
            # Rebalance if length difference exceeds 1
            if (len(l_max) - len(r_min)) > 1:
                top = heapq.heappop(l_max)
                top = top * (-1)
                heapq.heappush(r_min, top)
            
            elif (len(r_min) - len(l_max)) > 1:
                top = heapq.heappop(r_min)
                top = top * (-1)
                heapq.heappush(l_max, top)
            
            if len(l_max) == len(r_min):
                m = ((-1 * l_max[0]) + r_min[0]) / 2
                ans.append(m)
            
            elif len(l_max) > len(r_min):
                ans.append(-1*l_max[0])
            
            else:
                ans.append(r_min[0])
        
        return ans

    def hpush_min(self, arr, k):
            # Function to insert and heapify
            arr.append(k)

            idx = len(arr) - 1
            p = (idx - 1) // 2
            while idx != 0 and arr[p] > arr[idx]:
                arr[p], arr[idx] = arr[idx], arr[p]
                idx = p
                p = (idx - 1) // 2

    def hpush_max(self, arr, k):
            # Function to insert and heapify
            arr.append(k)

            idx = len(arr) - 1
            p = (idx - 1) // 2
            while idx != 0 and arr[p] < arr[idx]:
                arr[p], arr[idx] = arr[idx], arr[p]
                idx = p
                p = (idx - 1) // 2
        
    def down_heapify_min(self, arr, idx):
        # arr[0], arr[-1] = arr[-1], arr[0]
        # ret = arr.pop()
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
    
    def down_heapify_max(self, arr, idx):
        # arr[0], arr[-1] = arr[-1], arr[0]
        # ret = arr.pop()
        flag = True
        n = len(arr)

        while flag:

            maxi_ = idx

            l = 2 * idx + 1
            r = 2 * idx + 2

            if l < n and arr[l] > arr[maxi_]:
                maxi_ = l
            
            if r < n and arr[r] > arr[maxi_]:
                maxi_ = r
            
            if maxi_ != idx:
                arr[idx], arr[maxi_] = arr[maxi_], arr[idx]
                idx = maxi_
            
            else:
                flag = False
    
    def get_min(self, arr):
        arr[0], arr[-1] = arr[-1], arr[0]
        ret = arr.pop()
        self.down_heapify_min(arr, 0)
        return ret

    def get_max(self, arr):
        arr[0], arr[-1] = arr[-1], arr[0]
        ret = arr.pop()
        self.down_heapify_max(arr, 0)
        return ret