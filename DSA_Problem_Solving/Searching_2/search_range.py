'''Q3. Search for a Range
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description
Given a sorted array of integers A(0 based index) of size N, find the starting and ending position of a given integar B in array A.

Your algorithm's runtime complexity must be in the order of O(log n).

Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].



Problem Constraints
1 <= N <= 106

1 <= A[i], B <= 109



Input Format
The first argument given is the integer array A.
The second argument given is the integer B.



Output Format
Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].



Example Input
Input 1:

 A = [5, 7, 7, 8, 8, 10]
 B = 8
Input 2:

 A = [5, 17, 100, 111]
 B = 3


Example Output
Output 1:

 [3, 4]
Output 2:

 [-1, -1]


Example Explanation
Explanation 1:

 First occurence of 8 in A is at index 3
 Second occurence of 8 in A is at index 4
 ans = [3, 4]
Explanation 2:

 There is no occurence of 3 in the array.'''

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):

        f, l = self.find_first(A, B), self.find_last(A, B)

        return [f, l]

    def find_first(self, A, B):
        ans = -1
        s, e = 0, len(A) - 1

        while s <= e:
            mid = s + (e - s) // 2

            if A[mid] >= B:

                if A[mid] == B:
                    ans = mid
                e = mid - 1
            
            else:
                s = mid + 1
        
        return ans
    
    def find_last(self, A, B):
        ans = -1
        s, e = 0, len(A) - 1

        while s <= e:
            mid = s + (e - s) // 2

            if A[mid] > B:
                e = mid - 1
            
            else:
                if A[mid] == B:
                    ans = mid
                s = mid + 1

        return ans