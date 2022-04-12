'''Find longest palindromic substrings for all prefixes in a string
https://stackoverflow.com/questions/63532882/finding-the-lengths-of-the-longest-palindromic-substrings-for-all-prefixes-of-a
Ex. Given 'ababa'
Output 1 1 3 3 5
'a' : 'a' (1)
'ab: 'a' or 'b' (1)
'aba': 'aba' (3)
'abab': 'aba' or 'bab' (3)
'ababa': 'ababa' (5)
 
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        i, j = self.tabular(s)
        
        return s[i:j + 1] 
    
    def tabular(self, s):
        
        n = len(s)
        
        dp = [[0 for i in range(n)] for j in range(n)]
        
        ans1 = [float('-inf') for i in range(n)]
        
        ans = 1
        
        lft, rt = -1, -1
        
        for l in range(1, n + 1):
            
            for st in range(n - l + 1):
                
                e = l + st - 1
                
                if st == e:
                    dp[st][e] = 1
                
                elif e - st + 1 == 2:
                    
                    if s[st] == s[e]:
                        dp[st][e] = 1
                
                else:
                    
                    if s[st] == s[e] and dp[st + 1][e - 1]:
                        dp[st][e] = 1
                
                if dp[st][e] == 1:
                    
                    for r in range(n):
                        
                        if st >= 0 and e <= r:
                            
                            ans1[r] = max(ans1[r], e - st + 1)
                    
                    if l >= ans:
                        lft, rt = st, e
        
        print(ans1)
        return lft, rt

'''The above solution runs in O(N^3) due an additional inner loop filling up prefix values
   A better way would be to only update the cell at ans1[e]
   Later null cells in ans1 should be filled with the closest non null value on their left.'''

'''The below approach follows an expand around the center idea and then updates the final prefix array
   with the same idea as mentioned above. With this idea, time complexity drops to O(N^2) and space becomes O(1) as well
   The logic for finding longest substring in prefixes is not totally correct in the below solution'''

def pal_prefix(s):
    
    ans = [float('-inf') for i in range(len(s))]
    curr = 0
    inds = [-1, -1]
    for i in range(len(s)):
        
        low, high = i - 1, i + 1
        
        while low >= 0 and s[low] == s[i]:
            low -= 1
        
        while high < len(s) and s[high] == s[i]:
            high += 1
        
        while low >= 0 and high < len(s) and s[high] == s[low]:
            low -= 1
            high += 1
        
        low += 1
        high -= 1
        
        if (high - low + 1) > curr:
            curr = high - low + 1
            inds[0], inds[1] = low, high
            ans[high] = curr
    
    to_fill = ans[0]
    
    for i in range(1, len(s)):
        
        if ans[i] == float('-inf'):
            ans[i] = to_fill
        
        else:
            to_fill = ans[i]
    
    print(inds)
    print(ans)

'''Following is the DP solution which runs in O(N^2) time and space and correctly calculates all prefix lengths
   The ans1 list stores the final answer. There will be rows which won't be filled after the DP loops
   are done. We can initialize the first character prefixes value as 1. Then for all unfilled values
   to the right, fill them with the closest filled value to their left.'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        i, j = self.tabular(s)
        
        return s[i:j + 1] 
    
    def tabular(self, s):
        
        n = len(s)
        
        dp = [[0 for i in range(n)] for j in range(n)]
        
        ans1 = [float('-inf') for i in range(n)]
        
        ans = 1
        
        lft, rt = -1, -1
        
        for l in range(1, n + 1):
            
            for st in range(n - l + 1):
                
                e = l + st - 1
                
                if st == e:
                    dp[st][e] = 1
                
                elif e - st + 1 == 2:
                    
                    if s[st] == s[e]:
                        dp[st][e] = 1
                
                else:
                    
                    if s[st] == s[e] and dp[st + 1][e - 1]:
                        dp[st][e] = 1
                
                if dp[st][e] == 1:
                    
                    if e - st + 1 > ans:
                        
                        # Update the LPS length for prefix ending in e
                        ans = e - st + 1
                        ans1[e] = ans
                        lft, rt = st, e
        
        print(ans1)
        
        ans1[0] = 1
        
        to_fill = ans1[0]
    
        for i in range(1, len(s)):
        
            if ans1[i] == float('-inf'):
                ans1[i] = to_fill
        
            else:
                to_fill = ans1[i]
        
        print()
        print(ans1)
        return lft, rt