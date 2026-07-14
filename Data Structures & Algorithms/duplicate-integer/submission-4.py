class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort(key=None, reverse=False)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

#Strategy
# 1. Can approach similar to the Two Sum problem
# 2. Use two pointers. Assumption: the numbers are consecutive
# 3. Hmmm, worth checking. May not be necessary to include multiple loops
# 4. The pointer strategy technically works, but it isn't efficient

# Assume that the constraints are the numbers being in consecutive order, so we only need one pointer



        