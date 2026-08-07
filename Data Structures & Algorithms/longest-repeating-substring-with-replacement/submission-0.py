class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #hashmap - letters : counts
        res = 0 #holds result

        l = 0 #left pointer, start of window

        #right pointer - goes till the end
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) #starting first letter, we get its count from hashmap then increment it

            while (r-l+1) - max(count.values()) > k: # length of curr window - most frequent letter has to be less than k -> total allowed changes
                count[s[l]] -= 1 #if not, we decrement count of the first letter of curr window in hashpam
                l += 1 #and move l pointer forward
            res = max(res, r-l+1) #
        return res

#time complexity O(26*n) = O(n)
#space complexity 