class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resMap = {} 

        for i, n in enumerate(nums):  #i: index  n= value
            difference = target - n

            if difference in resMap:
                return[resMap[difference], i]
            
            resMap[n] = i
        
        return 
    
