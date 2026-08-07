class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()

        for n in nums:
            if n in numSet:
                return True
            else:
                numSet.add(n)
        
        return False

# time complexity O(n)
# space complexity O(n)