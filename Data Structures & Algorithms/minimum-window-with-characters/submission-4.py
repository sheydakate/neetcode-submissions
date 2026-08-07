class Solution:
    def minWindow(self, s: str, t: str)-> str:
        
        # s = ABDCBCA -> len = n        {A:1, B:0, D:0, C:1}  l=1, r=3
        # t = CBA     -> len = m        {A:1, B:1, C:1}   need = 3, have = 3

        resLen, resRange = float("inf"), [-1,-1] #when looking for max -> -infinity ,   for min -> +infinity (*the infinity later gets updated with real value once found)
                                                 #[-1,-1] is invalid range, will be updated when true range is found. if not found, it'll flag when returned
        countWindow, countT = {}, {}

        for c in t: # O(m)
            countT[c] = 1 + countT.get(c,0) #1st store everything needed in countT

        have, need = 0, len(countT)
        l = 0

        for r in range(len(s)):
            countWindow[s[r]] = 1 + countWindow.get(s[r], 0)

            if countWindow[s[r]] == countT.get(s[r], 0):
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    resRange = [l,r]
            
                countWindow[s[l]] -= 1
                if countWindow[s[l]] < countT.get(s[l], 0):
                    have -= 1
                l += 1
        
        l, r = resRange[0], resRange[1]
        return s[l:r+1] if resLen != float("inf") else ""


# time complexity O(n + m)
# space complexity O(n + m)