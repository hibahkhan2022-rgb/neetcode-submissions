class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Declare the anagrams
        s_anagram = {}
        t_anagram = {}
        #Loop thru anagrams and add keys -- make them the numbers
        if len(s) != len(t):
            return False
        else:
            for i in s:
                if i in s_anagram:
                    s_anagram[i] += 1
                else:
                    s_anagram[i] = 1
            for j in t: 
                if j in t_anagram:
                    t_anagram[j] += 1
                else:
                    t_anagram[j] = 1
            if s_anagram == t_anagram:
                return True
        return False
    

#Thought process:
# Since the frequency of the letters is the only thing that matters, use hash map; 
# Thinking about adding a key-value pair, then traversing through s and t
# Realization: what if s and t are arranging letters in different order?
# Question: Can we use .sort() for alphabetical order?, then use points moving at the same time
# Answer: We can actually just use the .keys() and .values() to see if they match

