class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()

        for n in nums:
            if not n in myset:
                myset.add(n)
            else: 
                return True
        
        return False
            


