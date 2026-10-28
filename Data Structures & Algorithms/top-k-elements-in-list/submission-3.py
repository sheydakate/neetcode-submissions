class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}

        for num in nums:
            myMap[num] = 1 + myMap.get(num, 0)
        
        arr = []

        for key, val in myMap.items():
            arr.append([val, key])
        
        arr.sort()
        
        res = []
        while len(res) < k:
            res.append (arr.pop()[1])
        
        return res