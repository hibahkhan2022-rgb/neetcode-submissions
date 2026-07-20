class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        count = 0
        new_list = []
        while count < 2:
            for number in nums:
                new_list += [number]
            count += 1
        return new_list

# Strategy
# I need to take an array and add it twice to a new list

