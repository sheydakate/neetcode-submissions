class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        arr = [0]*26
        
        for c in range(len(s)):
            arr[ord(s[c])- ord("a")] += 1 
            arr[ord(t[c])- ord("a")] -= 1
        
        for r in arr:
            if r != 0:
                return False
        else:
            return True
