class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        count = 0 

        NumSet = set(nums)

        for i in NumSet: 

            if (i - 1) not in NumSet: 
                length = 1

                while (i + length) in NumSet: 
                    length += 1
                count = max(length, count)
        
        return count
        