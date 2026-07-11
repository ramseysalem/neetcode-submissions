class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # returning indices not the actual values 
        # smaller index first, always 

        d = {}

        for i, n in enumerate(nums): # giving index and number values 
            target_value = target - n # getting a value we need to find in the dictionary 
            if target_value in d: 
                return [d[target_value], i] # if two values that can add to target are in dictionary, then return their indices
            else: 
                d[n] = i # add index and value if value not found and then repeat
        
            

        