class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):  #not same len, not anagrams
            return False
        
        countS, countT = {}, {}

        for i in range (len(s)):    #iterating thru one string ok cause they are the same length
            countS[s[i]] = 1 + countS.get(s[i], 0) #count occurences of each char in s, default val is 0
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True