class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()         #make a hash set

        for n in nums:          #loop, of length n
            if n in hashset:    #if n is found in hashset
                return True     #duplicate found
            hashset.add(n)      #if not found, add it to set
        return False            #exit loop, no duplicate