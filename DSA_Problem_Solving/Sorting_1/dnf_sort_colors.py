'''Dutch National Flag Algorithm
Sort an array containing only 0's, 1's and 2's

Works on two ideas:
Use three pointers to partition a region, low, mid and high
Everything to the left of low should be 0's
Everything to the right of high should be 2's
What remains between low and high would be 1's
'''

class Solution:
    # @param A : list of integers
    # @return nothing
    def solve(self, A):

        low, mid, high = 0, 0, len(A) - 1

        while mid <= high:
            
            # If mid finds a zero, swap it with A[low] and increment it
            if A[mid] == 0:
                A[mid], A[low] = A[low], A[mid]
                mid += 1
                low += 1
            
            # If a one is encountered at mid, do nothing

            # If a two is encountered at mid, swap with high and decrement high
            if A[mid] == 2:
                A[mid], A[high] = A[high], A[mid]
                high += 1
        