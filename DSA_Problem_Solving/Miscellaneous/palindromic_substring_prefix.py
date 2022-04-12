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

'''The below approach follows an expand around the center idea (considering odd (1 character) and even (2 characters)) palindromes
   and then updates the final prefix array with the same idea as mentioned above. With this idea, time complexity drops to 
   O(N^2) and space becomes O(1) as well if output array is not considered.
   For populating the largest palindromic substring, we need to fill up a[i] with the max(a[i], largest value seen on the left)
   This is needed as we are not updating subsequent answers and not all ending indices will constitute a valid palindrome
   '''   

def expand_center(st, start, end, cnt):
    
    ans = float('-inf')
    idx = [-1, -1]
    while start >= 0 and end < len(st) and st[start] == st[end]:
        
        l = end - start + 1
        
        if l > ans:
            cnt[end] = max(cnt[end], l)
            ans = l
            idx = [start, end]
        
        start -= 1
        end += 1
    
    if ans == float('-inf'):
        return 0, -1, -1
    
    return ans, idx[0], idx[1]
        
def pal_prefix(s):
    
    n = len(s)
    ans = [float('-inf') for i in range(n)]
    
    for i in range(n):
        
        l1, s_o, e_o = expand_center(s, i, i, ans)
        l2, s_e, e_e = expand_center(s, i, i + 1, ans)
    
    max_seen = ans[0]
    
    for i in range(1, n):
        ans[i] = max(max_seen, ans[i])
        max_seen = ans[i]
    
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