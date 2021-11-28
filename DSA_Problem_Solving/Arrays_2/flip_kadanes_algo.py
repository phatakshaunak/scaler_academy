'''Q3. Flip
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given a binary string A(i.e. with characters 0 and 1) consisting of characters A1, A2, …, AN. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, …, AR. By flipping, we mean change character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised.

If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.



Problem Constraints

1 <= size of string <= 100000



Input Format

First and only argument is a string A.



Output Format

Return an array of integers denoting the answer.



Example Input

Input 1:

A = "010"
Input 2:

A = "111"


Example Output

Output 1:

[1, 1]
Output 2:

[]


Example Explanation

Explanation 1:

A = "010"

Pair of [L, R] | Final string
_______________|_____________
[1 1]          | "110"
[1 2]          | "100"
[1 3]          | "101"
[2 2]          | "000"
[2 3]          | "001"

We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
Explanation 2:

No operation can give us more than three 1s in final string. So, we return empty array [].'''

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        
        max_sum, curr = 0, 0
        start, s = 0, 0
        
        for i in range(len(A)):
            
            if A[i] == '0':
                curr += 1
            else:
                curr += -1
            
            if curr > max_sum:
                start = s
                end = i
                max_sum = curr
            
            elif curr < 0:
                s = i+1
                curr = 0
        
        max_val = -1
        
        for val in A:
            if val == '0':
                max_val = max(max_val, 1)
            else:
                max_val = max(max_val, -1)
        
        if max_val == -1:
            return []
        
        else:
            return [start+1, end+1]
            
        # O(N) time, O(1) space
        
        #Convert the string by changing '0' to a 1 (contribution in the final array) and '1' to -1 in the final array. Then apply Kadane's algorithm to find subarray with maximum sum. Flipping this subarray will maximize the 1s in the original string
        
        # flip = []
        # for i in A:
        #     if i =='0':
        #         flip.append(1)
        #     else:
        #         flip.append(-1)
        
        # max_sum, curr = 0, 0
        # start, s = 0, 0
        
        # for j in range(len(flip)):
            
        #     curr += flip[j]
            
        #     if curr > max_sum:
        #         start = s
        #         end = j
        #         max_sum = curr
            
        #     if curr < 0:
        #         curr = 0
        #         s = j+1
        
        # if max(flip) < 0:
        #     return []
        # return [start+1,end+1]
        
# O(N) time, O(N) space