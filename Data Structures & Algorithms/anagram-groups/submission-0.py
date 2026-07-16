from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        result = []

        for s in strs:
            new_list = tuple(sorted(s))
            anagram_map[new_list].append(s)
        
        for values in anagram_map.values():
            result.append(values)
        
        return result

'''
Strategy:
1. For better memory management, take advantage of fixed-sized arrays
'''
