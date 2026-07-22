class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0
        
        # Walk through both strings
        while s_pointer < len(s) and t_pointer < len(t):
            # If the characters match, move the s pointer to look for the next letter
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                
            # Always move the t pointer forward to keep searching
            t_pointer += 1
            
        # If we successfully matched all characters in s, s_pointer will equal len(s)
        return s_pointer == len(s)
#Strategy 
# We need to first create a loop where letters loop through the s, and add to a list.

# 1st implementation: This does not account for duplicates right now
# 2nd implementation: Solves duplicates, but reintroduces issues of sort. Cannot be sorted because order matters