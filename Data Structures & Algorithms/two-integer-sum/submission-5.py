class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       myMap = {} #create hashmap

       for i, val in enumerate(nums):
            diff = target - val

            if diff in myMap:
                return [myMap[diff],i]
        
            myMap[val] = i

