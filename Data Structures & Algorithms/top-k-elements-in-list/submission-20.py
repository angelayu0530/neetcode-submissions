#Counters give the freq from min to max
# pushes all the values
#removes values with checking if len(min) > k, so we get the top k freq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) 
        min_heap = []  
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)  

        result = []
        for freq, num in min_heap:
            result.append(num)
        return result
