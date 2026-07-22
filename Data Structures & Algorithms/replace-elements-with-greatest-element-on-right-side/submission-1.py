class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = -1
    
    # Iterate from the last index down to 0
        for i in range(len(arr) - 1, -1, -1):
            original_value = arr[i]
            arr[i] = max_so_far
            max_so_far = max(max_so_far, original_value)
        
        return arr

            

# Strategy
# Here we need to iterate through the array and check if arr[i+1] > arr[i]
# If so, then we replace arr[i] = arr[i+1]. 
