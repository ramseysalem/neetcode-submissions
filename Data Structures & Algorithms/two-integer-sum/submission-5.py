class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dictionary = {} 

        for i, j in enumerate(nums): 
            difference = target - j 
            if difference in dictionary: 
                return [dictionary[difference], i]
            else: 
                dictionary[j] = i
        