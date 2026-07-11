class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # hashmap and if the count is greater than 2 for 
        # any value than it has to return True. 

        # I am thinking you could do some set manipulation but 

        # hash , key value 1, count 

        numHash = {}

        for n in nums:

            if n in numHash: 
                return True
            numHash[n] = 1
        
        return False



        