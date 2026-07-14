class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        

#start off with looping through the array -- use for i in range(), etc
# Have two pointers -- there should be an i and a j
# j can start at one point after the i
# let i loop first, then let j loop second. 
# if the combinations produce a viable result, return their indices

