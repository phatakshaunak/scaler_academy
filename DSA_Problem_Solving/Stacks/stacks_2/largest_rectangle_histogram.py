'''Q1. Largest Rectangle in Histogram
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A .

A represents a histogram i.e A[i] denotes height of the ith histogram's bar. Width of each bar is 1.

Find the area of the largest rectangle formed by the histogram.



Problem Constraints

1 <= |A| <= 100000

1 <= A[i] <= 1000000000



Input Format

The only argument given is the integer array A.



Output Format

Return the area of largest rectangle in the histogram.



Example Input

Input 1:

 A = [2, 1, 5, 6, 2, 3]
Input 2:

 A = [2]


Example Output

Output 1:

 10
Output 2:

 2


Example Explanation

Explanation 1:

The largest rectangle has area = 10 unit. Formed by A[3] to A[4].
Explanation 2:

Largest rectangle has area 2.'''

class Solution:
	# @param A : list of integers
	# @return an integer
	def largestRectangleArea(self, A):
        n = len(A)
        nsl, nsr = [0] * n, [0] * n
        st = []

        for i in range(n):
            
            # Equality to ensure we are considering same height histograms as well and not popping them
            while st and A[st[-1]] >= A[i]:
                st.pop()

            if st:
                nsl[i] = st[-1]
            else:
                nsl[i] = -1

            st.append(i)

        while st: st.pop()

        for j in range(n - 1, -1, -1):
            
            # Equality to ensure we are considering same height histograms as well and not popping them
            # Equality is needed either in nsl or nsr and not in both ; but does not matter here as we take 
            # a maximum value which will remain the same counting from both ends

            while st and A[st[-1]] >= A[j]:
                st.pop()
            
            if st:
                nsr[j] = st[-1]
            
            else:
                nsr[j] = n
            
            st.append(j)

        ans = float('-inf')

        for k in range(n):

            s = nsl[k] + 1
            e = nsr[k] - 1

            area = (e - s + 1) * A[k]

            ans = max(ans, area)
        
        return ans