class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # create a list of list [[][][]], within those lists, 
        # theres is a key, and based off of the index of those 
        # lists within lists is the frequnecy of those keys. 
        # so index 1 would be frequency 1, and within that index
        # is the list of keys that are frequnecy 1 

        count = {} 
        frequency = [[] for _ in range(len(nums)+1)]

        # initalize hashmap 

        for n in nums: 
            count[n] = count.get(n, 0) + 1

        # so now we have the keys and their frequencies. 
        # now we have to place them within the frequnecy list 


        for key, value in count.items():
            frequency[value].append(key)
        
        # now we have a frequency list filled with keys based off the idx

        result = []

        for l in frequency[::-1]:
            for n in l: 
                result.append(n)
                if k == len(result): 
                    return result
                



        
        