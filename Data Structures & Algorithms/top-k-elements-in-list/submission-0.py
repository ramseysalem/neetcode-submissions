class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {} 

        for num in nums: 
            
            if num not in hashmap: 
                hashmap[num] = 1 
            hashmap[num] += 1
        
        heap = [] 

        for num in hashmap.keys(): 
            heapq.heappush(heap, (hashmap[num], num))
            if len(heap) > k: 
                heapq.heappop(heap)
        
        result = [] 
        for i in range(k): 
            result.append(heapq.heappop(heap)[1])
        return result 


        