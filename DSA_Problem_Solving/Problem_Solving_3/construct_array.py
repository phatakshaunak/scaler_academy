'''Q3. Construct Array
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Simba has an integer array of length A. Despite having insisted alot, He is not ready to reveal the array to his friend Expert. But now, he is ready to reveal some hints about the array and challenges Expert to find the values of his hidden array. The hints revealed are as follows:

The array is sorted by values in ascending order.
All the elements in the array are distinct and positive (greater than 0).
The array contains two elements B and C such that B < C.
Difference between all adjacent (consecutive) elements are equal.
Among all the arrays satisfying the above conditions, his array has the minimum possible maximum element value.
If there are multiple possible arrays, his array will have minimum possible minimum element value.
Can you help Expert to construct such an array and surprise Simba?



Problem Constraints

2 <= A <= 50

1 <= B < C <= 50



Input Format

First argument is an integer A.

Second argument is an integer B.

Third argument is an integer C.



Output Format

Return a sorted integer array having length N, denoting Simba's Secret Array.



Example Input

Input 1:

 A = 5
 B = 20
 C = 50 
Input 2:

 A = 2
 B = 2
 C = 3 


Example Output

Output 1:

 [10, 20, 30, 40, 50]
Output 2:

 [2, 3]


Example Explanation

Explanation 1:

 Sorted array = [10, 20, 30, 40, 50] satisfies all the conditions having maximum value = 50 minimum possible.
 Other arrays such as [20, 30, 40, 50, 60] having max value = 60 or [20, 50, 80, 120] having max value = 120, also satisfy conditions but their maximum value is not minimum possible(As minimum possible max value is 50). 
Explanation 2:

 As the array has only 2 elements, [2, 3] is the only possible candidate.
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        
        i = 1
        factors = []
        
        while (i*i) <= (C-B):
            
            if (C-B) % i == 0:
                factors.append(i)
                
                if i * i != (C-B):
                    factors.append(int((C-B)/i))
            
            i += 1
        
        ans_a, ans_d = -1, -1
        
        factors.sort(reverse=True)
        
        for num in factors:
        
            a = C - ((A-1)*num)
            
            if (a > 0) and (a <= B):
                ans_a = a
                ans_d = num
                break
            
            elif a <= 0:
                
                while a <= 0:
                    a += num
    
                if (a > 0) and (a <= B):
                    ans_a = a
                    ans_d = num
        
        ans = []
        
        for i in range(A):
            term = ans_a + (i * ans_d)
            ans.append(term)
            
        return ans

    '''Arithmetic progression properties'''
        