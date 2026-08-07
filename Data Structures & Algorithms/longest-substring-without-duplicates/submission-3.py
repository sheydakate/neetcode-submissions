class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() #set to keep track of letters
        l, res = 0,0 #pointer , res saves result
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
                
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res

#time complexity O(n)
#space complexity O(n)