class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dictionary = {} 

        for i, j in enumerate(nums): 
            diff = target - j
            if diff in dictionary: 
                return [dictionary[diff], i]
            else: 
                dictionary[j] = i
        