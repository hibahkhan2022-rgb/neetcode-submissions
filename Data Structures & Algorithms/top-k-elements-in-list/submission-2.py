class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_anagram = {}
        result = []
        nums = tuple(nums)

        for number in nums: 
            if number not in freq_anagram:
                freq_anagram[number] = 1;
            else: 
                freq_anagram[number] += 1;
        
        # Sort the items by their frequency (value) in descending order
        sorted_items = sorted(freq_anagram.items(), key=lambda x: x[1], reverse=True)
        
        count = 0 
        for number, frequency in sorted_items:
            if count < k:
                result.append(number)
                count += 1
        return result
        
        


    
'''
Strategy:
1. Thinking about using a hashmap and mapping the whole list. 
2. Then traverse through the .values() and find the values that have the kth most frequent
3. If a value is found, add 1 to the coutner until it reaches the k value.
4. Append to a new list and return
'''