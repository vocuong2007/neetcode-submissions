class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        for num in nums:
            if num in count:
                count[num] +=1
            else:
                count[num] =1
        arr = list(count.keys())
        arr.sort(key=lambda x: count[x], reverse=True) 
        
        return arr[:k]