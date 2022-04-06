'''Given strings s1 and s2, C as boolean and l as an index,
If C is True, find if s1 exists in s2 as an independent word (spaces on both sides or one side if start/end of s2)
and whether the start index of s1's match in s2 >= l
If C is False, find if s1 exists anywhere (independent word/substring) in s2 as long as start index is >= l
Else, return a message as not found'''

def hack_match(s1, s2, C, l):
    
    n, m = len(s1), len(s2)
    
    for i in range(n - m + 1):
        
        idx = i
        flag = False
        
        for j in range(m):
            
            if s1[idx] != s2[j]:
                break
            
            idx += 1
            
            if j == m - 1 and i >= l:
                
                if C == 'N':
                    return i
                
                else:
                    if (i == 0 or i == n - m) or s1[i - 1] == ' ' and s1[idx] == ' ':
                        return i
        
    return 'Goodbye Watson'

def generate_Z(st):
    
    n = len(st)
    Z = [0 for i in range(n)]
    Z[0] = n
    L, R = 0, 0
    for i in range(1, n):
        
        if i > R:
            
            L, R = i, i
            while R < n and st[R] == st[R - L]:
                R += 1
            R -= 1
            Z[i] = R - L + 1
        
        else:
            idx = i - L
            
            if Z[idx] < R - i + 1:
                Z[i] = Z[idx]
            
            else:
                L = i
                
                while R < n and st[R] == st[R - L]:
                    R += 1
                R -= 1
                Z[i] = R - L + 1
    
    return Z

def hack_match_optimized(s1, s2, C, l):
    
    n, m = len(s1), len(s2)
    
    st = s2 + '#' + s1
    
    Z = generate_Z(st)
    
    for i in range(m + 1, len(st)):
        
        if Z[i] == m:
            
            if C == 'N' and i - m - 1 > l:
                return i - m - 1
            
            else:
                
                start = i - m - 1
                end = start + m - 1
            
                if start == 0 or end == len(st) - 1 or (s1[start - 1] == ' ' and s1[end + 1] == ' '):
                    
                    if i - m - 1 > l:
                        return i - m - 1
    
    return 'Goodbye Watson'

s1 = 'We love to hack on hackerearth'
s2 = 'hack'

# hack_match(s1, s2, 'N', 14)
hack_match_optimized(s1, s2, 'Y', 14)

