'''Q4. N/3 Repeat Number
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You're given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.
If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Example:

Input: [1 2 3 1 1]
Output: 1 
1 occurs 3 times which is more than 5/3 times.'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        
        c1, c2 = float("inf"), float("inf")
        ct1, ct2 = 0, 0
        
        for num in A:
            
            if c1 == num:
                ct1 += 1
            
            elif c2 == num:
                ct2 += 1
            
            elif ct1 == 0:
                c1 = num
                ct1 += 1
            
            elif ct2 == 0:
                c2 = num
                ct2 += 1
            
            else: 
            
                ct1 -= 1
                ct2 -= 1
        
        c1_check, c2_check = 0, 0
        
        for num in A:
            
            if num == c1:
                c1_check += 1
                
            elif num == c2:
                c2_check += 1
            
        if c1_check > (len(A) // 3):
            return c1
        
        elif c2_check > (len(A) // 3):
            return c2
        
        else:
            return -1

'''
Generalizing, we want to find a number that occurs more than N/k times in an array. At most there can be k-1 such numbers, eg. N/2, only 1;
N/3, at most 2 and so on.
The intuition here is that we maintain k containers for possible candidates. We traverse the array and increment the containers if we find
a candidate that we stored earlier. If we do not find any of the k candidates, that means we have found k distinct elements. We can safely
remove these from consideration as there won't be a N/k majority in this group of k. This is continued across the array and ultimately we
can end up with k possible candidates. If there exist such elements, the algorithm will return the correct answer. However, there can be
cases when there is no majority and these k containers would contain incorrect candidates. Thus the array needs to be traversed again to 
check the frequencies of the k candidates. The second traversal will take care of the case when we don't have any N/k majority elements.

Some good explanations: https://leetcode.com/problems/majority-element-ii/discuss/787595/voting-algorithm-with-explanation-for-k-3-and-generalization
https://leetcode.com/problems/majority-element-ii/discuss/860990/Detailed-Explanation-Intuition-behind-presence-of-atmost-2-majority-elements
https://cs.stackexchange.com/questions/91803/explaination-for-variation-of-boyer-moore-majority-voting-algorithm
'''
